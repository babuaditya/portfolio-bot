from typing import Text, Dict, Any
import requests
from .config import Config
import logger
logger = logging.getLogger(__name__)
class SlackNotifier:
    """Handles all Slack notifications"""
    
    def __init__(self):
        self.webhook_url = Config.SLACK_WEBHOOK_URL
        self.rasa_url = Config.RASA_SERVER_URL
    
    def send_handoff_notification(
        self, 
        sender_id: Text, 
        user_message: Text
    ) -> bool:
        """
        Send human handoff notification to Slack
        
        Args:
            sender_id: User's conversation ID
            user_message: The message that triggered handoff
            
        Returns:
            bool: True if notification sent successfully
        """
        slack_message = self._build_handoff_message(sender_id, user_message)
        logger.info(sender_id,user_message)
        try:
            response = requests.post(
                self.webhook_url,
                json=slack_message,
                headers={'Content-Type': 'application/json'},
                timeout=5
            )
            return response.status_code == 200
            
        except requests.exceptions.RequestException as e:
            logger.error(e)
            print(f"Error sending to Slack: {e}")
            return False
    
    def _build_handoff_message(
        self, 
        sender_id: Text, 
        user_message: Text
    ) -> Dict[Text, Any]:
        """Build Slack message payload"""
        
        reply_command = self._generate_reply_command(sender_id)
        
        return {
            "text": "🔔 Human Handoff Request",
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "🔔 Human Handoff Required"
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*User ID:*\n`{sender_id}`"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Timestamp:*\n{self._get_timestamp()}"
                        }
                    ]
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*User Message:*\n> {user_message}"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*To reply, use:*\n```{reply_command}```"
                    }
                }
            ]
        }
    
    def _generate_reply_command(self, sender_id: Text) -> Text:
        """Generate curl command for replying to user"""
        return (
            f"curl -X POST {self.rasa_url}/conversations/{sender_id}/messages \\\n"
            f"  -H 'Content-Type: application/json' \\\n"
            f"  -d '{{\"text\": \"Your reply here\"}}'"
        )
    
    @staticmethod
    def _get_timestamp() -> Text:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
