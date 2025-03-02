def initialize():
    user_name = input("Enter your name: ")

    welcome_msg = (
        f"Hello {user_name}! You will act as the moderator, facilitating a discussion between OpenAI and Llama. "
        "You can start by providing your name, a topic for the chat, and throughout the session, "
        "you may ask either model to respond."
    )

    print(welcome_msg)

    topic = input(f"{user_name}, please enter a topic name for the chat or type 'exit' to leave: ")

    if len(topic) <= 1:
        print(f"Invalid topic name: {topic}")
        return None, None

    if topic.lower() == 'exit':
        print("Exiting the program.")
        return None, None

    else:
        print(f"That's an interesting topic, {user_name}. The stage is all yours. Please type 'exit' to leave.")
        return user_name, topic
