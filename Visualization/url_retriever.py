from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import cohere
from langchain.llms import Cohere
import nltk
import json
from .serp import stats_finder
llm = Cohere(cohere_api_key="4aJ9yWbIrOzI2W5LZeLeIdin2AYMpkq18PffLuvi",temperature=0)
# import nltk
# nltk.download('averaged_perceptron_tagger')

def diseases(tex):
    prompt=f"write the mental disorders mentioned in {tex} if no mental disorders present say 'no disease found'"
    diseases=llm(prompt)
    nltk_tokens = nltk.word_tokenize(diseases)
    return nltk_tokens
    # print(nltk_tokens)

def impact_count(disease):
    # prompt2=f"tell me number of people suffering from {disease} no need to give background information"
    # return llm(prompt2)
    return stats_finder(disease)

def research_params(tex):
    prompt=f"""Give me a structured output in json format covering the aim,use of project, and the real world impact of this project and expand in detail on the impact {tex} 
 the project description is {tex}"""
    params=llm(prompt)
    params=json.loads(params)
    print(params["impact"])
    return params
    

# prompt_check=f"write 'yes' if any mental disorder is detected in {tex} otherwise return 'no'"
# print(llm(prompt_check))

def impact(url):
    urls = [url]
    loader = UnstructuredURLLoader(urls=urls)
    docs = loader.load()
    tex=str(docs[0])
    list_diseases=diseases(tex)
    print(list_diseases)
    
    if "no"not in list_diseases:
        disease_stats=""
        l=[]
        for i in list_diseases:
            
            link,stat=impact_count(i)
            d={"disease":i,"source":link,"impact":stat}
            l.append(d)
            # disease_stats=disease_stats+stat
        return l,"disease"
    else:
        params=research_params(tex)
        return params,"research"
        