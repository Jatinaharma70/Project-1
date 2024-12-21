import random

print("Welcome to the chatbot! Type 'exit' to quit")
#while True:
print("0. Snake")
print("-1. Water")
print("1. Wanted")
print("2. Gun")
    
    # Chatbot responses
responses = {
    "0": ["2 Losser ","1 Police ","-1 Snake "],
    "2": ["1 Win ☺️","2 Same to you","-1 someone"],
    "-1": ["0 snake win ","2 someone","1 no someone"],
    "1": ["-1 equal ","2 Kill him","0 safe"],
    "exit": ["Goodbye!", "See you later!", "Bye!"]
}
      
def chatbot():
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Computer:", random.choice(responses[user_input]))
        else:
            print("Chatbot: Sorry, I didn't understand that.")
        if responses  == "exit":
            break

chatbot()
      
