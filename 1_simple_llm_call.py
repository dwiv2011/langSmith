from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

import os

print("TRACING:", os.environ.get("LANGCHAIN_TRACING_V2"))
print("PROJECT:", os.environ.get("LANGCHAIN_PROJECT"))
print("API KEY:", os.environ.get("LANGCHAIN_API_KEY")[:5])
# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

model = ChatOpenAI()
parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | model | parser

# Run it
result = chain.invoke({"question": "What is the capital of India?"})
print(result)
