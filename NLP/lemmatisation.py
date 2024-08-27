from nltk.stem import WordNetLemmatizer
import nltk
# create an object of class WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("drive", 'v'))
print(lemmatizer.lemmatize("drove", 'v'))