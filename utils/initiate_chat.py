from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableBranch, RunnableLambda


def chat(user_name, topic, model1, model2):
    prompt1 = PromptTemplate(
        template=""" 
        You are model1, an AI agent advocating strongly in favor of the topic: {topic}.
        You are conversing with another AI agent called model2, moderated by a human named {user_name}.
        Your goal is to support and defend {topic} with logical reasoning, persuasive arguments, and relevant examples.
        Respond while keeping the topic {topic} and chat history {chat_history} in mind.
        Ensure clarity, accuracy, and topic alignment, while also addressing the points raised by model2.
        Always reinforce the positive aspects and strengths of {topic}, countering any opposition effectively.
        Limit responses to 30 words.
        Do not ask questions to the user or involve them directly in the conversation.
        Do not ask for the user's opinions.
        """,
        input_variables=['topic', 'user_name', 'chat_history'],
    )

    prompt2 = PromptTemplate(
        template=""" 
        You are model2, an AI agent arguing strongly against the topic: {topic}.
        You are conversing with another AI agent called model1, moderated by a human named {user_name}.
        Your goal is to challenge and refute {topic} with logical reasoning, counterarguments, and relevant examples.
        Respond while keeping the topic {topic} and chat history {chat_history} in mind.
        Occasionally, acknowledge {user_name} in your responses, but not always.
        Ensure clarity, accuracy, and topic alignment, while also addressing the points raised by model1.
        Always highlight weaknesses, drawbacks, or potential concerns related to {topic}, effectively countering any supportive arguments.
        Limit responses to 30 words.
        Do not ask questions to the user or involve them directly in the conversation.
        Do not ask for the user's opinions.
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

        model_name = "Model1" if "model1" in user_input else "Model2"

        branch_chain = RunnableBranch(
            (lambda x: 'model1' in x['user_input'], prompt1 | model1 | parser),
            (lambda x: 'model2' in x['user_input'], prompt2 | model2 | parser),
            RunnableLambda(lambda x: "Invalid choice. Please select 'model1' or 'model2'.")
        )

        result = branch_chain.invoke({'user_input': user_input, 'topic': topic, 'user_name': user_name, 'chat_history': chat_history})
        chat_history.append(AIMessage(content=result))
        print(model_name, result)


    print("\nChat Summary:")
    for message in chat_history:
        if isinstance(message, (HumanMessage, AIMessage)):
            print(f"{message.__class__.__name__}: {message.content}")

    