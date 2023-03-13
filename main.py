from fastapi import FastAPI, Body                        #Body permite escribir datos en el body instead of requirements
from fastapi.responses import HTMLResponse               #HTMLResponse es para integrar un codigo html en una respuesta 
from pydantic import BaseModel                           #BaseModel es para hacer una clase para las peliculas   
from typing import Optional                              #Optional permite establecer una condicion como opcional             


app = FastAPI()
app.title = 'Mi app con FastAPI'
app.version = '0.0.1'

class Movie(BaseModel):
    id: Optional[int] | None = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    }, 
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]


@app.get('/', tags = ['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            return item
    return 'Not a registered number'

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str):   
    return [item for item in movies if item['category'] == category ]

@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies
  
@app.put('/movies/{id}', tags=['movies'])
def update_movie(id:int, movie: Movie):
    for item in movies:
        if item['id'] == movie.id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return movies

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return movies