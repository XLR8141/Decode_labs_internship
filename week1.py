import sys

def run_chatbot():
    print("==============  Rule Based AI Chatbot ==============")
    
    while True:
        raw_input = input("You: ")
        clean_input = raw_input.lower().strip()
        
        if clean_input == "exit" or clean_input == "quit":
            print("Chatbot: Goodbye! Ending the continuous loop.")
            break
            
        elif clean_input == "hello" or clean_input == "hi":
            print("Chatbot: Hello! I am your rule-based AI assistant.")
            
        elif clean_input == "what is your goal?":
            print("Chatbot: My goal is to respond to predefined user inputs using logic.")
            
        elif clean_input == "who created you?":
            print("Chatbot: I was created by an AI Engineer at DecodeLabs.")
            
        elif clean_input == "what is a white box?":
            print("Chatbot: A white box system is a program where the logic is clear and has zero mystery.")
            
        elif clean_input == "help":
            print("Chatbot: You can say hello, ask about my goal, ask about white boxes, or type 'exit'.")
        
        else:
            print("Chatbot: I'm sorry, that input does not match any of my hard-coded rules.")

if __name__ == "__main__":
    run_chatbot()