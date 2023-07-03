# from langchain.prompts import PromptTemplate
# prompt_template = """Use your entire knowledge along with the given context to answer the question

# {context}

# Question: {question}
# Answer in Italian:"""
# PROMPT = PromptTemplate(
#     template=prompt_template, input_variables=["context", "question"]
# )


# chain_type_kwargs = {"prompt": PROMPT}
# embeddings = CohereEmbeddings(cohere_api_key="4aJ9yWbIrOzI2W5LZeLeIdin2AYMpkq18PffLuvi")
# docsearch = Chroma.from_documents(docs, embeddings)
# qa = RetrievalQA.from_chain_type(llm=llm, 
#                                     chain_type="stuff",
#                                     retriever=docsearch.as_retriever(),
#                                     chain_type_kwargs=chain_type_kwargs)

# query = "what is the best indian movie of all time"
# print(qa.run(query))