class Movie: #Created a class w/properties of a Movie
    def __init__(self,movieName,rating,yearReleased): #initializes the properties and creates the template used for Instances
        self.movieName=movieName
        self.rating=rating
        self.yearReleased=yearReleased
    def __str__(self): #used to print all properties of the object
        newPrint=(f"Movie info: {self.movieName}, {self.rating}, {self.yearReleased}")
        return newPrint
class Product:
    def __init__(self,price,quantity,name):
        self.price=price
        self.quantity=quantity
        self.name=name
    def __str__(self):
        productPrint= (f"Product Info: {self.price}, {self.quantity}, {self.name}")
        return productPrint

def main(): #function to be called
    movie1= Movie("Little RAscals","5 stars",1995) #Instantiate the class Movie
    movie2=Movie("Beauty and The Beast","3 Stars", 1986)
    print(movie1) #Displays the instance in the terminal
    print(movie2)

    product1=Product(124.99,5,"Gamecube")
    product2=Product(280.99,7,"Xbox 360")
    print(product1)
    print(product2)

main() #function is called