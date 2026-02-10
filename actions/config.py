import os

class Config:
    """Configuration for human handoff and Slack integration"""
    
    SLACK_WEBHOOK_URL = os.getenv(
        "SLACK_WEBHOOK_URL", ''
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
        if "h" in Config.SLACK_WEBHOOK_URL:
            raise ValueError("SLACK_WEBHOOK_URL not configured properly")
        return True
