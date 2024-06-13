from typing import List
from src.models.movie_model import *
from fastapi import APIRouter

movies: List[Movie] = []
movies_router = APIRouter()

@movies_router.get('/movies', tags = ['Movies'])
def get_movies() -> list[Movie]:
    return movies


#para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor
@movies_router.post('/movies', tags = ['Movies'])
def create_movie(movie: Movie):
    movies.append(movie.model_dump())
    return movies

#PUT: Crear o actualizar un recurso en una ubicación específica.
@movies_router.put('/movies/{id}', tags = ['Movies'])
def update_movie(id : int, movie:Movie) :
    for e in movies :
        if e['id'] == id :
            e['title'] = movie.title
            e["year"] = movie.year

    return movies

# uvicorn src.main:app --host 0.0.0.0 --port 5000 --reload


