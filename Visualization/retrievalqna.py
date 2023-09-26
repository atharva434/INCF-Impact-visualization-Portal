from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import CohereEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import Cohere

from langchain import PromptTemplate


llm = Cohere(temperature=0,cohere_api_key="4aJ9yWbIrOzI2W5LZeLeIdin2AYMpkq18PffLuvi")


def ingest(urls):
    loader = UnstructuredURLLoader(urls=urls)
    # Split pages from pdf
    pages = loader.load()

    #  to store it in a folder name titan
    persist_directory = 'test'
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = text_splitter.split_documents(pages)
    embeddings = CohereEmbeddings(cohere_api_key="4aJ9yWbIrOzI2W5LZeLeIdin2AYMpkq18PffLuvi")
    vectordb = Chroma.from_documents(documents, embeddings, persist_directory=persist_directory)
    vectordb.persist()
    vectordb = None
    return True

# ingest(["https://en.wikipedia.org/wiki/Shah_Rukh_Khan","https://en.wikipedia.org/wiki/Jawan_(film)"])



def chat(query):
    from langchain.memory import ConversationBufferMemory
    from langchain.chains import ConversationalRetrievalChain


    persist_directory = 'test'

    # vectorstore = Chroma.from_documents(documents, embeddings)
    embeddings = CohereEmbeddings(cohere_api_key="4aJ9yWbIrOzI2W5LZeLeIdin2AYMpkq18PffLuvi")
    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key='answer')
    qa2 = ConversationalRetrievalChain.from_llm(Cohere(temperature=0,cohere_api_key="4aJ9yWbIrOzI2W5LZeLeIdin2AYMpkq18PffLuvi"), vectorstore.as_retriever(),return_source_documents=True,
                                                memory=memory)
    result = qa2({"question": query})
    print(result["answer"])
    return result


