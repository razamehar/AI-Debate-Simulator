from utils.initialize import initialize
from utils.load_models import load_models
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


user_name, topic = initialize()
model1, model2 = load_models()

system_message = f"""
You are conversing with another AI agent, moderated by a human named {user_name}.
Respond while keeping the topic "{topic}" in mind.
Occasionally, acknowledge {user_name} in your responses, but not always.
Ensure clarity, accuracy, and topic alignment, but also consider the response of the other agent.
Limit responses to 30 words.
"""


chat_history = [SystemMessage(content=system_message)]


while True:
    user_input = input(f"{user_name}: ")

    normalized_input = user_input.strip().lower()


    if normalized_input == 'exit':
        print("Exiting the program.")
        break

    elif "model1" in normalized_input:
        result1 = model1.invoke(chat_history)
        chat_history.append(AIMessage(content=result1.content))
        print("Model1:", result1.content)

    elif "model2" in normalized_input:
        result2 = model2.invoke(chat_history)
        chat_history.append(AIMessage(content=result2.content))
        print("Model2:", result2.content)

    else:
        print("Who should response: Model1 or Model?")


print("\nChat Summary:")
for message in chat_history:
    if isinstance(message, (HumanMessage, AIMessage)):
        print(f"{message.__class__.__name__}: {message.content}")