from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import sys
sys.path.append("./")
from configs import settings
import os
def get_chat_model():
    """
    The function `get_chat_model` returns a ChatHuggingFace model with specified parameters.
    :return: An instance of the ChatHuggingFace class with the specified parameters llm, repo_id,
    temperature, max_new_tokens, and huggingfacehub_api_token is being returned.
    """
    return ChatHuggingFace(llm=HuggingFaceEndpoint(
        repo_id=settings.MODEL_REPO_ID,
        temperature=settings.TEMPERATURE,
        max_new_tokens=settings.MAX_TOKENS,
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
        ))