""" I started developing the chatbot to be run on python, but when I started to have it run on a server, locally hosted using Xampp, I needed to make some changes
to how the chatbot could take in input and return a reponse, using Flask, python web framework to handle requests from Xampp server, typically from user input on
the webpage"""




import json
import re
import requests

chatbot_url = 'http://127.0.0.1:8080/send_message'
"""import random_responses"""
from difflib import get_close_matches


# Load JSON data
def load_knowledge_base(file_path:str) -> dict:
    with open(file_path,'r') as file:
        data:dict = json.load(file)
        return data

def send_message(message):
    payload = {'message': message}
    response = requests.post(chatbot_url, json=payload)

    if response.status_code == 200:
        print('Message sent successfully')
    else:
        print('Failed to send message')
"""# Store JSON data
response_data = load_knowledge_base("bot.json")
"""

def save_knowledge_base(file_path:str,data:dict):
    with open (file_path,'w') as file:
        json.dump(data,file,indent=2)

def find_best_match(user_question:str, questions: list[str]) -> str | None:
    matches: list= get_close_matches(user_question, questions, n=2, cutoff=0.80)
    return matches[0] if matches else None

def get_answer_for_question(question:str, bot:dict) -> str | None:
  for q in bot["questions"]:
    if q["question"] == question:
      return q["answer"]

"""def chat_bot():     for running in python use this instead of def process_message(message:str)"""
    def process_message(message:str):
    bot: dict = load_knowledge_base("bot.json")
    print("Bot: Hi, I am your personal chatbot, How can I help you? \nIf you want to exit the conversation at any time, please enter quit")
    while True:
        
        """user_input: str = input("You: ")"""
        user_input: str = message
        """if user_input.lower() == "quit":  //for running in python
            break """
        best_match: str | None = find_best_match(user_input, [q["question"] for q in bot["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, bot)
            print(f'Bot:{answer}')
        else:
            print('Bot: I don\'t know the answer, Could you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip this question: ')

            if new_answer.lower() != 'skip':
                bot["questions"].append({"question":user_input,"answer":new_answer})
                save_knowledge_base("bot.json",bot)
                print('Bot: Thank you for teaching me!')

if __name__=='__main__':
   """ send_message("Hi")"""
    chat_bot()
 
