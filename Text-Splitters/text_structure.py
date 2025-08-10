from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text="""
A space program is a coordinated effort by a government, private organization, or international partnership to explore and utilize outer space for scientific, technological, and commercial purposes. Space programs often involve the development of spacecraft, satellites, launch vehicles, and supporting infrastructure.

Early space programs, such as the Soviet Union’s Vostok program and the United States’ Mercury program, focused on achieving milestones like the first human in space and the first Moon landing. Over time, these programs have expanded to include planetary exploration, space telescopes, space stations, and deep-space missions.

Today, organizations like NASA, ESA, Roscosmos, ISRO, CNSA, and private companies such as SpaceX and Blue Origin are advancing space technology. Their goals include Earth observation, communications, scientific research, asteroid mining, lunar bases, and eventual human missions to Mars."""

splitter= RecursiveCharacterTextSplitter(
    chunk_size=350,
    chunk_overlap=0
)
chunks=splitter.split_text(text)
print(len(chunks))
print(chunks[0])