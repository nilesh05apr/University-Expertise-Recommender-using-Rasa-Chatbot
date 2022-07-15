# University-Expertise-Recommender-using-Rasa-Chatbot

*This is an experimental project built using rasa.ai opensource module for building chatbots.*  


To WEB Scrap :  
- create virtual envireomnent (optional)    
- git clone https://github.com/nilesh05apr/University-Expertise-Recommender-using-Rasa-Chatbot  
- pip install -r requirements  
- cd University-Expertise-Recommender-using-Rasa-Chatbot  
- cp .env-template .env  
- add your mongo db uri in .env  
- cd webscrap  
- python3 settings.py  
- python3 scrap.py  

To Run ChatBot:  
- inside University-Expertise-Recommender-using-Rasa-Chatbot directory    
- rasa shell   
- or pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple    
- rasa x  

For more information:    
https://towardsdatascience.com/building-a-chatbot-with-rasa-3f03ecc5b324    
https://rasa.com/blog/category/tutorials/  
