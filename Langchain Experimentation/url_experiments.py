from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import cohere
from langchain.llms import Cohere
import nltk
llm = Cohere(cohere_api_key="4aJ9yWbIrOzI2W5LZeLeIdin2AYMpkq18PffLuvi",temperature=0)
# import nltk
# nltk.download('averaged_perceptron_tagger')
urls = [
    "https://www.thevirtualbrain.org/tvb/zwei"
]

loader = UnstructuredURLLoader(urls=urls)

docs = loader.load()
tex=str(docs[0])


def diseases(tex):
    
    prompt=f"write the mental disorders mentioned in {tex} if no mental disorders present say 'no disease found'"
    diseases=llm(prompt)
    nltk_tokens = nltk.word_tokenize(diseases)
    return nltk_tokens
    # print(nltk_tokens)

def impact_count(disease):
    prompt2=f"tell me number of people suffering from {disease} no need to give background information"
    return llm(prompt2)

# prompt_check=f"write 'yes' if any mental disorder is detected in {tex} otherwise return 'no'"
# print(llm(prompt_check))
list_diseases=diseases(tex)
print(list_diseases)
if "no"not in list_diseases:
    for i in list_diseases:
        print(impact_count(i))

else:
    print("sorry")

