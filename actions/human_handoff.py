from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, ConversationPaused
from .slack_notifier import SlackNotifier
from .config import Config


class ActionHumanHandoff(Action):
    """Action to handoff conversation to human agent"""
    
    def __init__(self):
        super().__init__()
        self.slack_notifier = SlackNotifier()
    
    def name(self) -> Text:
        return "action_human_handoff"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """Execute human handoff"""
        
        # Extract conversation details
        user_message = tracker.latest_message.get('text', 'No message')
        sender_id = tracker.sender_id
        
        # Log handoff attempt
        self._log_handoff(sender_id, user_message)
        
        # Send notification to Slack
        success = self.slack_notifier.send_handoff_notification(
            sender_id, 
            user_message
        )
        
        # Respond to user
        if success:
            dispatcher.utter_message(text=Config.HANDOFF_MESSAGE)
            return self._create_handoff_events()
        else:
            dispatcher.utter_message(text=Config.HANDOFF_ERROR_MESSAGE)
            return []
    
    @staticmethod
    def _log_handoff(sender_id: Text, message: Text) -> None:
        """Log handoff for analytics"""
        print(f"[HANDOFF] User: {sender_id} | Message: {message}")
    
    @staticmethod
    def _create_handoff_events() -> List[Dict[Text, Any]]:
        """Create events for handoff state"""
        return [
            SlotSet("handoff_to_human", True),
            ConversationPaused()
        ]


class ActionResumeFromHandoff(Action):
    """Action to resume conversation after human handoff"""
    
    def name(self) -> Text:
        return "action_resume_from_handoff"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """Resume normal conversation flow"""
        
        dispatcher.utter_message(
            text="Conversation resumed. How can I help you?"
        )
        
        return [SlotSet("handoff_to_human", False)]
