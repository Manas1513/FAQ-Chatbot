from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

with open('faqs.json', 'r') as f:
    faqs = json.load(f)

questions = list(faqs.keys())
answers = list(faqs.values())

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_response(query, threshold=0.3):
    vec = vectorizer.transform([query])
    sim = cosine_similarity(vec, X)
    max_sim_index = sim.argmax()
    if sim[0][max_sim_index] > threshold:
        return answers[max_sim_index]
    else:
        return "This seems like a complex query. Redirecting to human support..."
