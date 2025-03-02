from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


def load_models():
    load_dotenv()


    model1 = ChatOpenAI(max_tokens = 40)
    model2 = ChatOpenAI(max_tokens = 40)

    return model1, model2
