from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.vectorstores import Chroma
from langchain.schema import Document
from dotenv import load_dotenv
load_dotenv()
doc1=Document(
    page_content="Virat Kholi is one of the most successful and consitent batsman in IPL history. Known for his aggressive batting",
    metadata={"team":"Royal Challengers Banglore"}
)
doc2=Document(
    page_content="Rohit Sharma is one of the most successful captain in IPL history,leading Mumbai Indians to five titles.He's known for his calm batting",
    metadata={"team":"Mumbai Indians"}
)
doc3=Document(
    page_content="MS Dhoni,famously known as Captain cool,has led Chennai Super Kings to multiple IPL titles.His finshing skills,and wicket-keeping skills are best in this world.",
    metadata={"team":"Chennai Super Kings"}
)
docs=[doc1,doc2,doc3]

vector_store=Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory='chroma_db',
    collection_name='sample'
)
vector_store.add_documents(docs)
print(vector_store.get(include=['embeddings','documents','metadatas']))
print(vector_store.similarity_search(
    query='Who among is best is captian',
    k=1
))