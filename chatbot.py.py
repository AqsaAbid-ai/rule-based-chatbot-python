#Rule based AI chatbot

import datetime
import time


name=input("enter your name:")
presenthour=datetime.datetime.now().hour

if 5 <= presenthour <= 11:
   print("Good morning", name)
elif 11 <= presenthour <= 17:
   print("Good afternoon",name)
elif 17 <= presenthour <= 20:
   print("Good evening",name)
else:
   print("Good night", name)

print("Welcome to your chatBot")
print("You can ask me basic questions, Type 'bye' to exit from the bot")

#chatbot memory creation

responses={
    "hello":"Hi,welcome.How can i help you?",
    "how are you": "I am fine.Thank you",
    "who are you":"I am smart AI chatbot",
    "motivate me":"keep going. Every bug of your project makes you a better developer",
    "happy":"great to hear that",
    "bye":"Goodbye! Have a nice day.",
}

#method/Functions to get response of chatbot

def getresponseBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return "I am not able to tell that yet, I am learning soon"

# Take user input


while True:
   userinput=input("please ask your question:")
   reply=getresponseBot(userinput)
   print("Bot response:",reply)

   if 'bye'in userinput.lower():
    break


