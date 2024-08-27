import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords


# inject documents here
corpus = [

    "The quick brown fox jumps over the lazy dog. The dog barks.",

    """It was once the most common fox in the eastern United States, 
    and though still found there, human advancement and deforestation 
    allowed the red fox to become the predominant fox-like canid. 
    Despite this post-colonial competition, the gray fox has been able to 
    thrive in urban and suburban environments, one of the best examples 
    being southern Florida.
    The Pacific States and Great Lakes region still have the gray 
    fox as their prevalent fox.""".strip()
]

nltk.download('stopwords')

# Create a TfidfVectorizer object
vectorizer = TfidfVectorizer()

# Fit and transform the document
tfidf_matrix = vectorizer.fit_transform(corpus)

# Get feature names (terms)
feature_names = vectorizer.get_feature_names_out()

stop_words = set(stopwords.words('english'))

tfidf_arr: numpy.ndarray = tfidf_matrix.toarray()

document_index = 0

# Get TF-IDF values
for arr in tfidf_arr:

    print(f"Index of processed document in the corpus: {document_index}")

    document_index += 1

    # Create a dictionary to store term and TF-IDF value pairs
    tfidf_dict = dict(zip(feature_names, arr))

    # Sort the dictionary by TF-IDF values in descending order
    sorted_tfidf = sorted(tfidf_dict.items(), key=lambda item: item[1], reverse=True)

    # Print the sorted TF-IDF values
    for term, tfidf in sorted_tfidf:
    # Exclude words without a meaning
        if term not in stop_words:
           print(f"{term}: {tfidf}")