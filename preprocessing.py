from nltk.corpus import stopwords
import string # builtin string module 

stopword_list = stopwords.words('english')

def clean_message(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    text = [word for word in text.split() if word not in stopword_list]
    text = ' '.join(text)
    return text

