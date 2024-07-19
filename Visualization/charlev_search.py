import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Project,FProject

def char_n_gram(text, n):
    """
    This function generates n-grams from the text.
    Args:
        text: The text to generate n-grams from.
        n: The size of the n-gram.
    Returns:
        A list of n-grams from the text.
    """
    return [text[i:i+n] for i in range(len(text) - n + 1)]

def char_vectorize(text):
    """
    This function creates a character n-gram vector for the text.
    Args:
        text: The text to vectorize.
    Returns:
        A dictionary representing the character n-gram frequencies.
    """
    char_counts = Counter(char_n_gram(text, 2))  # Use bigrams (2-char n-grams)
    total_chars = sum(char_counts.values())
    return {char: count / total_chars for char, count in char_counts.items()}

def text_search_char(query):
    """
    This function performs character-level search using character n-grams.
    Args:
        query: The search query.
        documents: A list of documents to search in.
    Returns:
        A list of tuples (document, similarity_score).
    """

    # Fetch all projects
    projects = FProject.objects.all()
    
    # Combine the fields of each project into a single string
    documents = [project.combined_fields() for project in projects]
    
    char_vectors = [char_vectorize(text) for text in (documents + [query])]

    ranked_documents = []
    for i, doc in enumerate(documents):
        doc_vec = char_vectors[i]
        query_vec = char_vectors[-1]
        score = sum(min(doc_vec.get(char, 0), query_vec.get(char, 0)) for char in query_vec)
        ranked_documents.append((projects[i], score, projects[i].id))

    ranked_documents.sort(key=lambda x: x[1], reverse=True)

    # Return top 3 results
    return ranked_documents[:4]