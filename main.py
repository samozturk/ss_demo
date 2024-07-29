from fastapi import FastAPI
import random

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

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/cities")
async def test(n:int = 5):
    random_cities = random.sample(european_cities, n)
    return {"random_cities": random_cities}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



