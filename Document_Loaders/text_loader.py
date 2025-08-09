from langchain_community.document_loaders import TextLoader

loader= TextLoader('cricket_info.txt',encoding='utf-8')
docs=loader.load()
print(docs[0].page_content)