"""
Song  id,moviename,title,trackno,singer,duration
        -setsong(id,moviename,title,trackno,singer,duration)
        -getsong()
"""

class Song:

    id:int
    moviename:str
    title:str
    trackno:int
    singer:str
    duration:str

    def __init__(self,id,moviename,title,trackno,singer,duration):

        self.id = id
        self.moviename = moviename
        self.title = title
        self.trackno = trackno
        self.singer = singer
        self.duration = duration

    def get_song(self):

        print(self.id,self.moviename,self.title,self.trackno,self.singer,self.duration)

koodeppirannor_instance = Song(1,"Vaazha 2","Koodeppirannor",22,"Parvathi Pradeep","4 min")
mayajaalame_instance = Song(2,"Sarvam Maya","Maayajalame",10,"Justin Prabhakaran","4.30 min")

koodeppirannor_instance.get_song()
mayajaalame_instance.get_song()