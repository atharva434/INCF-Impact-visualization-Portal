import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import FProject

def text_search(query):
    # Fetch all projects
    projects = FProject.objects.all()
    
    # Combine the fields of each project into a single string
    documents = [project.combined_fields() for project in projects]
    
    # Combine the query with the documents
    all_texts = documents + [query]
    
    # Vectorize the text using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Compute cosine similarity between the query and all documents
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Get similarity scores
    scores = cosine_sim[0]
    
    # Rank documents based on similarity scores
    ranked_indices = np.argsort(scores)[::-1]
    ranked_scores = scores[ranked_indices]
    
    # Create a list of tuples (project, similarity_score)
    ranked_projects = [(projects[int(i)], ranked_scores[idx], projects[int(i)].id) for idx, i in enumerate(ranked_indices[:4])]
    
    return ranked_projects