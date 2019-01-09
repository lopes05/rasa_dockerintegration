from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import traceback
import requests
import configparser
from rasa_core.events import AllSlotsReset

from rasa_core_sdk.events import UserUtteranceReverted, ActionExecuted, ActionReverted

class ActionAskBirthDate(Action):
    def name(self):
        return "action_ask_birthdate"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("quando você nasceu?")
        
        return []