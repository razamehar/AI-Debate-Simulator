# Chat between two AI Models

This project enables a human moderator to oversee a conversation between two AI models, Model1 and Model2, on a specified topic. The system prompts the moderator to set the topic and allows them to decide which model responds at each turn. By calling Model1 or Model2, the moderator directs the discussion, ensuring both perspectives are explored. The entire conversation is logged for review after the session.
## Description

The system allows the user to:
1. Initialize the conversation with a user name and topic.
2. Load two AI models to participate in the conversation.
3. Maintain a chat history with messages from both models and the user.
4. Choose which model should respond during the conversation.
5. Print the chat history at the end of the session.

## Code Flow

1. **Initialization:**
   - The `initialize` function sets up the user name and topic.
   - The `load_models` function loads the two AI models (`model1` and `model2`).

2. **System Message:**
   - The system sends an introductory message, detailing the structure of the conversation. It specifies that responses should be based on the topic and interact with both models.

3. **User Interaction:**
   - The user inputs a message.
   - The system checks if the input mentions "model1" or "model2" to decide which model should respond.
   - The selected model's response is appended to the chat history.
   - The user can type "exit" to end the conversation.

4. **Chat History:**
   - The conversation is stored in `chat_history`, and once the conversation ends, the history is displayed.

## Features

- User can interact with two models and guide the conversation by choosing which model should respond.
- The conversation is logged and can be reviewed later.
- The system is highly modular with separate functions for initialization and model loading.

## Requirements

- Python 3.x
- langchain_core
- AIs models for `model1` and `model2`

## How to Run

1. Ensure that the required dependencies are installed.
2. Run the script.
3. Enter input commands when prompted, such as:
   - "Model1" or "Model2" to make one of the AI models respond.
   - "exit" to end the conversation.

## Example Usage

```bash
$ python conversation_system.py
Enter your name: Raza
Hello Raza! You will act as the moderator, facilitating a discussion between OpenAI and Llama. You can start by providing your name, a topic for the chat, and throughout the session, you may ask either model to respond.
Raza, please enter a topic name for the chat or type 'exit' to leave: Can AI surpass human level intelligence?
That's an interesting topic, Raza. The stage is all yours. Please type 'exit' to leave.
Raza: What do you have to say about the topic, Model1?
Model1: It's possible for AI to match human intelligence in specific tasks, yet surpassing overall human intelligence is still debated due to consciousness, creativity, and emotional understanding.
Raza: Do you agree with the above statement, Model2? Or, do you disagree?
Model2: Agreed. While AI can excel in certain areas, aspects like intuition, empathy, and common sense remain challenging to replicate comprehensively.

...

## License
This project is licensed under the Raza Mehar License. See the LICENSE.md file for details.

## Contact
For any questions or clarifications, please contact Raza Mehar at [raza.mehar@gmail.com].
