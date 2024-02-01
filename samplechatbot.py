def get_chatbot_response(message):
    responses = {
        "hi": "Hello! How can I help you?",
        "how are you?": "I'm a bot, but I'm doing well! How can I help you?",
        "bye": "Goodbye! Have a great day!"
    }

    # Make the message lowercase to make the chatbot case-insensitive
    message = message.lower()

    return responses.get(message, "I'm sorry, I don't understand that.")


def main():
    print("Welcome to the Chatbot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        response = get_chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
