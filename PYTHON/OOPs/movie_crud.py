


class MovieWise:

    def __init__(self):

        self.movies = [
            {"id":1,"title":"khalifa","year":2026,"genre":"action thriller","rating":8,"run_time":160,"director":"vysakh"}
        ]

    def post(self,**kwargs):

        required_fields = {"id","title","year","genre","rating","run_time","director"}
        missing__fields = required_fields.difference(kwargs.keys())

        if missing__fields:
            raise ValueError(missing__fields,"are missing")

        self.movies.append(kwargs)
        print("Record has been added....")

    def get(self):

        if len(self.movies)==0:
            print("No record found")

        else:
            for movie in self.movies:
                print(movie)

    def retrieve(self,id=None):

        if not id:
            raise ValueError("id missing")

        else:
            return [movie for movie in self.movies if movie.get("id")==id]

    def put(self,id=None,**kwargs):

        log = [movie for movie in self.movies if movie.get("id")==id][0]
        log.update(kwargs)

        print("Record updated")
        print(log)

    def delete(self,id=None):

        log = [movie for movie in self.movies if movie.get("id")==id][0]
        self.movies.remove(log)

        print("Record deleted")
        self.get()

movie_instance = MovieWise()

movie_instance.post(id=2,title="Thudarum",year=2023,genre="thriller",rating=9,run_time=185,director="Tharun Moorthy")
movie_instance.post(id=3,title="Oddyssey",year=2026,genre="adventure",rating=9.5,run_time=140,director="Nolan")
# movie_instance.get()

# print(movie_instance.retrieve(id=2))

# movie_instance.put(id=1,title="KGF",rating=9.5)

# movie_instance.delete(id=3)

    


