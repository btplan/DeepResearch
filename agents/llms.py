from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
api_key = os.getenv("DASHSCOPE_API_KEY")
model = "qwen3-max"

# 大模型接口三要素：base_url、api_key、model
llm = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model=model,
    temperature=1.2,
    # presence_penalty=0.5,
)


def get_llm():
    return llm
