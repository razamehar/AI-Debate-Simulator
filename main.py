from utils.initialize import initialize
from utils.load_models import load_models
from utils.initiate_chat import chat


user_name, topic = initialize()
model1, model2 = load_models()
chat(user_name, topic, model1, model2)

