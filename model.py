# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from Head.mouth import speak            

# # Initialize NLP tools
# stemmer = PorterStemmer()
# stop_words = set(stopwords.words('english'))

# # Load your Q&A dataset from a text file 1 usage

# def load_dataset(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         lines = file.read().split('\n')
#         qna_pairs = [line.strip().split(':') for line in lines if ':' in line]
#         dataset = [{'question': q.strip(), 'answer': a.strip()} for q, a in qna_pairs]
#     return dataset

# # Preprocess the text for usage
# def preprocess_text(text):
#     tokens = word_tokenize(text.lower())
#     tokens = [stemmer.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
#     return ' '.join(tokens)

# # Train the TF-IDF vectorizer
# 1 usage
# def train_tfidf_vectorizer (dataset):
# corpus = [preprocess_text(qa['question' ]) for qa in dataset] 
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(corpus)
# return vectorizer, X

# I

# # Retrieve the most relevant answer

# 1 usage
# def get_answer(question vectorizer X dataset):
# question = preprocess_text (question)
# question_vec = vectorizer.transform([question])
# similarities = cosine_similarity(question_vec, X)
# best_match_index = similarities.argmax()
# return dataset[best_match_index] ['answer']

# #Main function
# def mind(text):
# # Replace 'your_dataset.txt' with the path to your Q&A dataset
# dataset_path = r'C:\Users\vlogp\Desktop\Jarvis Ai\Data\text\qna_Data.txt'
# dataset = Load_dataset(dataset_path)

# vectorizer, X = train_tfidf_vectorizer(dataset)
# user_question = text
# answer = get_answer(user_question, vectorizer, X, dataset)
# SPEAK(answer)

# while True:
# x = input()
# mind(x)

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from Head.mouth import speak


# Initialize NLP tools
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))


# Load Q&A dataset
def load_dataset(file_path):
    dataset = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if ":" not in line:
                continue

            question, answer = line.split(":", 1)

            dataset.append({
                "question": question.strip(),
                "answer": answer.strip()
            })

    return dataset


# Preprocess text
def preprocess_text(text):
    tokens = word_tokenize(text.lower())

    tokens = [
        stemmer.stem(token)
        for token in tokens
        if token.isalnum() and token not in stop_words
    ]

    return " ".join(tokens)


# Train TF-IDF
def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(item["question"]) for item in dataset]

    vectorizer = TfidfVectorizer()

    X = vectorizer.fit_transform(corpus)

    return vectorizer, X


# Find best answer
def get_answer(question, vectorizer, X, dataset):

    processed_question = preprocess_text(question)

    question_vector = vectorizer.transform([processed_question])

    similarities = cosine_similarity(question_vector, X)

    best_index = similarities.argmax()

    confidence = similarities[0][best_index]

    if confidence < 0.25:
        return None

    return dataset[best_index]["answer"]


# Main function
def mind(text):

    dataset_path = r"C:\Users\ACER\OneDrive\Desktop\MJ\Dtata\brain_data\qna_data.txt"

    dataset = load_dataset(dataset_path)

    vectorizer, X = train_tfidf_vectorizer(dataset)

    answer = get_answer(text, vectorizer, X, dataset)

    return answer


# Run forever
if __name__ == "__main__":

    while True:

        user = input("You: ")

        if user.lower() in ["exit", "quit", "bye"]:
            speak("Goodbye, sir.")
            break

        mind(user)
