import os

class Config:
    """Configuration for human handoff and Slack integration"""
    
    SLACK_WEBHOOK_URL = os.getenv(
        "SLACK_WEBHOOK_URL", 
        "https://hooks.slack.com/services/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"
    )
    
    RASA_SERVER_URL = os.getenv(
        "RASA_SERVER_URL", 
        "http://localhost:5005"
    )
    
    HANDOFF_MESSAGE = "Connected to our team. They'll respond shortly."
    HANDOFF_ERROR_MESSAGE = "Couldn't connect to support. Please try again."
    
    @staticmethod
    def validate():
        """Validate required configuration"""
        if "https://hooks.slack.com/services/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" in Config.SLACK_WEBHOOK_URL:
            raise ValueError("SLACK_WEBHOOK_URL not configured properly")
        return True
