
#import langchain
import os


# OPENAI_API_KEY="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"
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY



from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator






# # 3. Crear el LLM
# from langchain.chat_models import ChatOpenAI
# llm = ChatOpenAI(temperature=0,model_name='gpt-3.5-turbo')


import openai
import dotenv
#dotenv.load_env()
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain


# Schema
schema = {
    "properties": {
        "name": {"type": "string"},
        "height": {"type": "integer"},
        "hair_color": {"type": "string"},
    },
    "required": ["name", "height"],
}

# Input 
inp = """Alex is 5 feet tall. Claudia is 1 feet taller Alex and jumps higher than him. Claudia is a brunette and Alex is blonde."""

# Run chain
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
chain = create_extraction_chain(schema, llm)
chain.run(inp)




# loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
# #index = VectorstoreIndexCreator().from_loaders([loader])

# data = loader.load()
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
# all_splits = text_splitter.split_documents(data)



# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import Chroma

# vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())