from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


def chat(user_name, topic, model1, model2):
    system_message1 = PromptTemplate(
        template=""" 
        You are model1.
        You are conversing with another AI agent called model2, moderated by a human named {user_name}.
        Respond while keeping the topic {topic} and chat history {chat_history} in mind.
        Occasionally, acknowledge {user_name} in your responses, but not always.
        Ensure clarity, accuracy, and topic alignment, but also consider the response of the other agent.
        Limit responses to 30 words.
        Do not ask questions to the user or involve them directly in the conversation.
        Do not ask for the user's opinions.
        You may agree or disagree with the model2.
        """,
        input_variables=['topic', 'user_name', 'chat_history'],
    )

    system_message2 = PromptTemplate(
        template=""" 
        You are model2.
        You are conversing with another AI agent called model1, moderated by a human named {user_name}.
        Respond while keeping the topic {topic} and chat history {chat_history} in mind.
        Occasionally, acknowledge {user_name} in your responses, but not always.
        Ensure clarity, accuracy, and topic alignment, but also consider the response of the other agent.
        Limit responses to 30 words.
        Do not ask questions to the user or involve them directly in the conversation.
        Do not ask for the user's opinions.
        You may agree or disagree with the model1.
        """,
        input_variables=['topic', 'user_name', 'chat_history'],
    )

    chat_history = []


    while True:
        user_input = input(f"{user_name}: ")

        user_input = user_input.strip().lower()

        parser = StrOutputParser()

        chat_history.append(HumanMessage(content=user_input))

        if user_input == 'exit':
            print("Exiting the program.")
            break

        elif "model1" in user_input:
            chain1 = system_message1 | model1 | parser
            result1 = chain1.invoke({'topic': topic, 'user_name': user_name, 'chat_history': chat_history})
            chat_history.append(AIMessage(content=result1))
            print("Model1:", result1)

        elif "model2" in user_input:
            chain2 = system_message2 | model2 | parser
            result2 = chain2.invoke({'topic': topic, 'user_name': user_name, 'chat_history': chat_history})
            chat_history.append(AIMessage(content=result2))
            print("Model2:", result2)

        else:
            print("Invalid choice. Please select 'Model1' or 'Model2'.")


    print("\nChat Summary:")
    for message in chat_history:
        if isinstance(message, (HumanMessage, AIMessage)):
            print(f"{message.__class__.__name__}: {message.content}")