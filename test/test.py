import requests
import numpy as np


r = requests.get("http://127.0.0.1:8000/city_summary?city=Porto")
city_summary = r.json()
summary1 = city_summary['Porto']

r = requests.get("http://127.0.0.1:8000/city_summary?city=Istanbul")
city_summary = r.json()
summary2 = city_summary['Istanbul']

r = requests.get(f"http://127.0.0.1:8000/embeddings?sentence={summary1}")
embeddings_json = r.json()
porto_embeddings = (np.array(embeddings_json['cls']))

r = requests.get(f"http://127.0.0.1:8000/embeddings?sentence={summary2}")
embeddings_json = r.json()
istanbul_embeddings = (np.array(embeddings_json['cls']))

r = requests.get(f"http://127.0.0.1:8000/similarity?sent1={summary1}&sent2={summary2}")
similarity_score = r.json()
similarity_score = similarity_score['similarity_score']
print(f"The similarity score between {summary1} and {summary2} is {similarity_score}")