from fastapi import FastAPI, Body
from src.routers.movies_route import movies_router

app = FastAPI()

@app.get('/', tags = ['Home'])

def home():
    return "Hello"

app.include_router(router = movies_router)


@app.get('/movies/{id}', tags=['Home'])
def get_movie(id: int):
    return id

#Parametro query
@app.get('/movies/', tags=['Home'])
def get_movie_by_category(category: str):
    return category
