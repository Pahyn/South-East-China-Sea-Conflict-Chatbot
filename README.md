# South-East-China-Sea-Conflict-Chatbot
A chatbot developed using Rasa-nlu and MongoDB to give information about current South East China Conflict  

To run the chatbot training open new terminal and run this code

python -m rasa_core.run -d models/dialogue -u models/nlu/default/weathernlu --endpoints endpoints.yml
