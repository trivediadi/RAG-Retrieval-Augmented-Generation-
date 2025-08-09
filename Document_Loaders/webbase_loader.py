from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

url='https://www.amazon.com/Smartphone-Unlocked-Processor-Manufacturer-Warranty/dp/B0DP3G4GVQ?ref=dlx_deals_dg_dcl_B0DP3G4GVQ_dt_sl14_e7_pi&pf_rd_r=D2DV6G90MYXG0HEPYX66&pf_rd_p=996f2b05-9e88-4ece-8de8-467770dc3be7&th=1'
loader=WebBaseLoader(url)
model=ChatOpenAI(model="gpt-3.5-turbo")
parser=StrOutputParser()
docs=loader.load()

prompt=PromptTemplate(
    template='Answer the following qustion \n{question} from the following text',
    input_variable=['question']
)

chain =prompt|model|parser
result=chain.invoke({'question':'what is the product best features and give only one of the best'})
print(result)