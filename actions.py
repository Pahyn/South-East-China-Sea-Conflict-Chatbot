# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
import random
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

logger = logging.getLogger(__name__)

class ActionGreet(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot('name').capitalize()
        seed = random.randint(0,1)
        response1 = """ Welcome {} to SECSC Bot. I'am specialized in inform you about current situation in South East China Sea Conflict. You may used abbrevation 'SECSC' or 'secsc' in your question. Let's go!""".format(name)
        response2 = """ Hi {}, my name is SECSC Bot. I'am trained to inform you about the situation in South East China Sea Conflict. You may used abbrevation 'SECSC' or 'secsc' in your question. Let's Start.""".format(name)   
        response = [response1,response2]
        dispatcher.utter_message(response[seed])
        #return response[seed]
        return [SlotSet("name", name)]