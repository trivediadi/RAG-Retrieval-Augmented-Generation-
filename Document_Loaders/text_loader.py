from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()


model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)
parser = StrOutputParser()

prompt=PromptTemplate(
    template="Write a summary about this {text}",
    input_variable="text"
)

loader= TextLoader('cricket_info.txt',encoding='utf-8')
docs=loader.load()

chain=prompt|model|parser

result=chain.invoke({"text":docs[0].page_content})
print(result)