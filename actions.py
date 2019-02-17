from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet



class ActionWeather(Action):

    def name(self):
        return 'action_weather'

    def run(
        self,
        dispatcher,
        tracker,
        domain,
        ):
        from apixu.client import ApixuClient
        api_key = '3d60663e4540463fb2272623182811'  # your apixu key
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        current = client.getCurrentWeather(q=loc)

        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']

        response ="""It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph. Powered by APIxu""".format(condition, city, temperature_c, humidity, wind_mph)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]

class MongoAction(Action):

    def name(self):
        return 'action_mongo'

    def __init__(self):

        from pymongo import MongoClient
        client = MongoClient('mongodb://localhost:27017')
    
        db = client["SECSC"]
        self.collection = db["conflict"]


    def run(self,dispatcher,tracker,domain):
        
        loc = tracker.get_slot('location')
        cursor = self.collection.find_one({"location": loc})

        desc = cursor["description"]
        claim = cursor["claim"]

        response = """{} is {}""".format(desc,claim)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]