from fastapi import FastAPI
import random
from wiki_funcs import get_wiki_summary
from vector_calcs import calculate_similarities, sent_embedding


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/city_summary")
def wiki_text(city:str):
    return {city: get_wiki_summary(city)}

@app.get("/embeddings")
def get_embeddings(sentence:str):
    embeddings = sent_embedding(sentence)
    
    return {'cls': embeddings[0].tolist(), 'ppol': embeddings[1].tolist()}

@app.get("/similarity")
def calculate_embeddings(sent1: str, sent2: str):
    similarity_score = calculate_similarities(sent1, sent2)
    return {'similarity_score': similarity_score}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


