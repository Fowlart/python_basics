from sklearn.feature_extraction.text import CountVectorizer

# Sample text data
documents = [
    "Artur is the best Data Engineer in the county!"
]

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit the model and transform the documents into a Bag of Words
bow_matrix = vectorizer.fit_transform(documents)

# Get the feature names (unique words in the corpus)
feature_names = vectorizer.get_feature_names_out()

# Convert the Bag of Words matrix into an array
bow_array = bow_matrix.toarray()

# Display the Bag of Words
print("Feature Names (Words):", feature_names)
print("\nBag of Words Representation:")
print(bow_array)