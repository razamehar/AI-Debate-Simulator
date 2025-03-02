# AI Conversation Moderation System

This project involves a conversation between two AI models, moderated by a human, with a clear topic in mind. The system allows a human to input commands and choose which AI model (Model1 or Model2) should respond. The conversation is logged and can be reviewed after the session ends.

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
[User input]: "What do you think about the topic?"
[System Response]: Model1: Response from Model1
[User input]: "Now Model2"
[System Response]: Model2: Response from Model2
...
