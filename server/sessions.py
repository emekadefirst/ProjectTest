from models import Product
from sqlmodel import Session, select
from db import engine

"""Product session manager"""    
def add_product(name, quantity, price, description, image, country):
    with Session(engine) as session:
        product = Product(name=name, quantity=quantity, price=price, description=description, image=image, country=country)
        session.add(product)
        session.commit()
        return "Product added Successfully"

def search_products(query: str):
    with Session(engine) as session:
        statement = select(Product).where(Product.name.contains(query))
        results = session.exec(statement).all()
        return results
    
    
def all_product():
    with Session(engine) as session:
        statement = select(Product)
        results = session.exec(statement).all()
        return results
    
def get_by_id():
    with Session(engine) as session:
        product = session.exec(Product).filter(Product, id).all()
        return product

def update_product(product_id, name=None, quantity=None, price=None, description=None, image=None, country=None):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if product:
            if name is not None:
                product.name = name
            if quantity is not None:
                product.quantity = quantity
            if price is not None:
                product.price = price
            if description is not None:
                product.description = description
            if image is not None:
                product.image = image
            if country is not None:
                product.country = country
            session.add(product)
            session.commit()
            return "Product updated successfully"
        else:
            return "Product not found"

def delete_product(product_id: int):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if product:
            session.delete(product)
            session.commit()
            return product
        else:
            return None