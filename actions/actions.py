from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher, ActionExecutor
from rasa_sdk.events import SlotSet

# Import modular actions
from .human_handoff import ActionHumanHandoff, ActionResumeFromHandoff
from .config import Config

print("Loading custom actions...")
class ActionGreetUser(Action):
    """Example action for greeting"""
    
    def name(self) -> Text:
        return "action_human_handoff"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        user_name = tracker.get_slot("user_name")
        
        if user_name:
            message = f"Hello {user_name}! How can I help you today?"
        else:
            message = "Hello! How can I help you today?"
        
        dispatcher.utter_message(text=message)
        
        return []


# Validate configuration on import
try:
    Config.validate()
except ValueError as e:
    print(f"Configuration Error: {e}")
