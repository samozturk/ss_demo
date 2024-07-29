import random
import wikipedia
from transformers import pipeline
import numpy as np

european_cities = [
    "Porto",
    "Krakow",
    "Edinburgh",
    "Dubrovnik",
    "Reykjavik",
    "Bruges",
    "Salzburg",
    "Tallinn",
    "Seville",
    "Bologna",
    "Ljubljana",
    "Zurich",
    "Copenhagen",
    "Bratislava",
    "Gothenburg",
    "Marseille",
    "Bucharest",
    "Cologne",
    "Riga",
    "Thessaloniki"
]

random_cities =random.sample(european_cities, 3)
results = wikipedia.search(random_cities[0])
wiki_pagename = results[0]
page_content = wikipedia.summary(wiki_pagename)
page_content

pipeline = pipeline('feature-extraction', model='xlnet-base-cased')
data = pipeline(page_content)

data_array = np.array(data)
print(data_array.shape)