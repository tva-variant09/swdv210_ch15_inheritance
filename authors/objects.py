from dataclasses import dataclass

# must be coded before Book class, as Book class has an Authors type hint
# isn't a data class because has an attribute that's a list
class Authors:
    def __init__(self):
        self.__list = []

    def add(self, author):
        self.__list.append(author)

    @property
    def count(self):
        return len(self.__list)
    
    #added to return the full name of the author
    def __str__(self):
        authors:str = ""
        for author in self.__list:
            authors += str(author) + ", "
        return authors[:-2] # slicing operation to remove the last comma and space characters
    
    # added to iterate through the list of authors
    def __iter__(self):
        for author in self.__list:
            yield author
    
@dataclass
class Book:
    title:str = ""
    authors:Authors = None
    
    # added to return the title of the book
    def __str__(self):
        return f"{self.title} by {self.authors}"
    
@dataclass
class Author:
    firstName:str = ""
    lastName:str = ""
    
    # added to return the full name of the author
    def __str__(self):  
        return f"{self.firstName} {self.lastName}" 



