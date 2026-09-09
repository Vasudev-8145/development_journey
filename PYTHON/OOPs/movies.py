"""
Movie title,language,year,director,genre 
    -setmovie(title,language,year,director,genre)
    -getmovie(self)
"""

class Movie:

    title:str
    language:str
    year:int
    director:str
    genre:str

    def __init__(self,title,language,year,director,genre):

        self.title = title
        self.language = language
        self.year = year
        self.director = director
        self.genre = genre

    def get_movie(self):

        print(self.title,self.language,self.year,self.director,self.genre)

thudarum_instance = Movie("Thudarum","Malayalam",2025,"Tharun murthy","Crime drama")
odissey_instance = Movie("Odissey","English",2026,"Nolan","Mythological fantasy")

thudarum_instance.get_movie()
odissey_instance.get_movie()
