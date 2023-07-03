from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import cohere
from langchain.llms import Cohere
llm = Cohere(cohere_api_key="4aJ9yWbIrOzI2W5LZeLeIdin2AYMpkq18PffLuvi")
# import nltk
# nltk.download('averaged_perceptron_tagger')
urls = [
    "https://www.thevirtualbrain.org/tvb/zwei"
]

loader = UnstructuredURLLoader(urls=urls)

docs = loader.load()
embeddings = CohereEmbeddings(cohere_api_key="4aJ9yWbIrOzI2W5LZeLeIdin2AYMpkq18PffLuvi")
docsearch = Chroma.from_documents(docs, embeddings)
qa = RetrievalQA.from_chain_type(llm=llm, 
                                    chain_type="stuff",
                                    retriever=docsearch.as_retriever())

query = "Description of this link provided in 80 words"
print(qa.run(query))