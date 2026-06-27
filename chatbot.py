def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. How can I assist you today?")

    while True:
        user=input(" You: ").lower()

        if user=="hello":
            print("Chatbot: Hellooo!")

        elif user=="how are you?":
                print("Chatbot: I am fine, Thank you!")

        elif user=="what is your name?":
            print("Chatbot: My name is Chatbot!")

        elif user=="bye":
            print("Goodbye! have a great day")
            break
        else:
            print("Chatbot: I am sorry, I didn't understaand that.")
chatbot();