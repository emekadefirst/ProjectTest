from sqlmodel import SQLModel, Field
from db import create_db_and_table
 
class Product(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, default=None, max_length=50)
    quantity: int
    price: float
    description: str
    image: str
    country: str = Field(default=None, max_length=50)  

create_db_and_table()