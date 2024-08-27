from sklearn.feature_extraction.text import TfidfVectorizer

# Your corpus of documents
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

# Create a TfidfVectorizer object
vectorizer = TfidfVectorizer()

# Fit the vectorizer on the entire corpus
vectorizer.fit(corpus)

# Get feature names (terms)
feature_names = vectorizer.get_feature_names_out()

# Get IDF values directly
idf_values = vectorizer.idf_

# Create a dictionary to store term and IDF value pairs
idf_dict = dict(zip(feature_names, idf_values))

# Sort the dictionary by IDF values in descending order
sorted_idf = sorted(idf_dict.items(), key=lambda item: item[1], reverse=True)

# Print the sorted IDF values
for term, idf in sorted_idf:
    print(f"{term}: {idf}")