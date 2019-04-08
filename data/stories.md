## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye
 
## story_name
* name{"name":"Sam"}
 - action_greet

 ## story_general_information
* general_information
 - utter_general_information

## story_9_dash_line
* 9_dash_line
 - utter_9_dash_line

 ## story_eez
* eez
 - utter_eez
 
## story_name
* name
 - action_greet
 
## story_joke_02
* greet
    - utter_name
 * name{"name": "Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
    - slot{"name": "lucy"}
    - action_greet
    - slot{"name": "Lucy"}
* goodbye
 - utter_goodbye
 
## story_general_information_02
* greet
    - utter_name
* name{"name": "joseph"}
    - slot{"name": "joseph"}
    - action_greet
    - slot{"name": "Joseph"}
* general_information
    - utter_general_information
* goodbye
    - utter_goodbye


## Generated Story -1915490559193332303
* greet
    - utter_name
* name{"name": "john"}
    - slot{"name": "john"}
    - action_greet
    - slot{"name": "John"}
* general_information
    - utter_general_information
* eez
    - utter_eez
* goodbye
    - utter_goodbye
    
## Generated Story -5894160409737502681
* greet
    - utter_name
* name{"name": "johnny"}
    - slot{"name": "johnny"}
    - action_greet
    - slot{"name": "Johnny"}
* 9_dash_line
    - utter_9_dash_line
* goodbye
    - utter_goodbye

## Generated Story -327902260335957343
* greet
    - utter_name
* name{"name": "farhin"}
    - slot{"name": "farhin"}
    - action_greet
    - slot{"name": "Farhin"}
* general_information
    - utter_general_information
* eez
    - utter_eez
* 9_dash_line
    - utter_9_dash_line
* goodbye
    - utter_goodbye

## Generated Story -8469899374942221535
* greet
    - utter_name
* name{"name": "farhin"}
    - slot{"name": "farhin"}
    - action_greet
    - slot{"name": "Farhin"}
* general_information
    - utter_general_information
* goodbye
    - utter_goodbye

## Generated Story -6268874800365627437
* greet
    - utter_name
* name{"name": "allie"}
    - slot{"name": "allie"}
    - action_greet
    - slot{"name": "Allie"}
* general_information
    - utter_general_information
* eez
    - utter_eez
* goodbye
    - utter_goodbye

## Generated Story 7945190348167551724
* greet
    - utter_name
* name{"name": "johnny"}
    - slot{"name": "johnny"}
    - action_greet
    - slot{"name": "Johnny"}
* 9_dash_line
    - utter_9_dash_line
* goodbye
    - utter_goodbye

## Generated Story 1678978326310713640
* greet
    - utter_name
* name{"name": "john"}
    - slot{"name": "john"}
    - action_greet
    - slot{"name": "john"}
* eez
    - utter_eez
* goodbye
    - utter_goodbye

