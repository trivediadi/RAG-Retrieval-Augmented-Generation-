from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("russia_vs_usa.pdf")
docs=loader.load()
print(docs[1].metadata)