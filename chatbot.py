print("welcome to Ai chatbot")
print("type exit to stop the chatbot.")

while True:
    user_input = input("you: ").lower()

    if user_input == "exit":
        print("Neo: Good bye have a nice day!")
        break

    elif user_input == "hello" or user_input == "hi":
        print("Neo: Hello sir. How can i help you")
        
    elif user_input == "how are you":
        print("Neo: I am fine, thank you.")

          
    elif user_input == "what is your name":
        print("Neo: My name is Neo AI.")
    
    elif user_input == "What is python":
        print("Neo:Python is a popular programming language used for AI, web development, and automation. ")

    elif "ai" in user_input:
        print("Neo: AI means Artificial Intelligence. It helps computers perform tasks like humans.")
    
    elif "LLM" in user_input:
        print("Neo: LLM is an AI model trained on a huge amount of text data so it can understand and generate human-like language.")

    elif "help" in user_input:
        print("Neo: You can ask me about AI, LLM, Python, my name, or say hello.")
    
    else:
        print("Neo: Sorry, I don't understand that yet.")