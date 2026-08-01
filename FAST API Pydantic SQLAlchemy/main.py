from fastapi import Depends, FastAPI
from models import Product
from dbConfig import Session, engine
from sqlalchemy.orm import Session as DBSession
import dbmodels

app = FastAPI()

dbmodels.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to my website"

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

def db_init():
    db = Session() 

    count = db.query(dbmodels.Product).count
    if count == 0:
        for product in products:  
            db.add(dbmodels.Product(**product.model_dump())) 
        db.commit()

db_init()

# @app.get("/products")
# def getAllProducts():
#     # db = Session() # DB Connection
#     # db.query()  # Then, execute queries
#     return products

# Updated getAllProducts with database Dependency Injection and SQL Alchemy
# Read

@app.get("/products")
def getAllProducts(db: DBSession = Depends(get_db)):
    db_products = db.query(dbmodels.Product).all()

    return db_products


# Dynamic data fetching use {}
# @app.get("/product/{id}")
# def getProductById(id: int, db: DBSession = Depends(get_db)):
#     for product in products:
#         if product:
#             return product

#     return "Product not found"

# Updated getProductById with database Dependency Injection and SQL Alchemy
# Specific Read
@app.get("/product/{id}")
def getProductById(id: int, db: DBSession = Depends(get_db)):
    db_product = db.query(dbmodels.Product).filter(dbmodels.Product.id == id).first()
    if db_product:
        return db_product

    return "Product not found"


# Data adding using POST
# @app.post("/product")
# def addProduct(product: Product):
#     products.append(product)
#     return product

# Updated addProduct with database Dependency Injection and SQL Alchemy
# Create
@app.post("/product")
def addProduct(product: Product, db: DBSession = Depends(get_db)):
    db.add(dbmodels.Product(**product.model_dump()))
    db.commit()
    return product


# Update Method
# @app.put("/product")
# def updateProduct(id: int, product: Product):
#     for i in range(len(products)):
#         if products[i].id == id:
#             products[i] = product
#             return "Product added successfully"
    return "No product Found"

# Updated updateProduct with database Dependency Injection and SQL Alchemy
# Update
@app.put("/product")
def updateProduct(id: int, product: Product, db: DBSession = Depends(get_db)):
    db_product = db.query(dbmodels.Product).filter(dbmodels.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product updated Successfully"
    else:
        return "Product Not Found" 

# # Delete Method
# @app.delete("/product")
# def deleteProduct(id: int):
#     for i in range(len(products)):
#         if products[i].id == id:
#             del products[i]
#             return "Product Deleted"
#     return "Product Not found"

# Updated deleteProduct with database Dependency Injection and SQL Alchemy
# Delete 
@app.delete("/product")
def deleteProduct(id: int, db: DBSession = Depends(get_db)):
    db_product = db.query(dbmodels.Product).filter(dbmodels.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted"
    else:
        return "Product Not found"