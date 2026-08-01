from pydantic import BaseModel #Import base model

class Product(BaseModel): #Inherit base model
    id: int
    name: str
    description: str
    price: float
    quantity: int

# Now we dont need this constructor

    # def __init__(self, id: int, name: str, description: str, price: float, quantity: int):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity