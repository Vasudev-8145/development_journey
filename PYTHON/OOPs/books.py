"""
class books
"""

class Book:

    title:str
    price:float
    pages:int
    author:str

    def __init__(self,title,price,pages,author):

        self.title = title
        self.price = price
        self.pages = pages
        self.author = author

    def get_book(self):

        print(self.title,self.price,self.pages,self.author)

rm_instance = Book("Randamoozham",650,500,"MT")
ar_instance = Book("Arachar",782,400,"KR Meera")

rm_instance.get_book()
ar_instance.get_book()