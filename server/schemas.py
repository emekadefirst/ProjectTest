from pydantic import BaseModel

class SearchProduct(BaseModel):
    query: str
    
class AddProduct(BaseModel):
    name: str
    quantity: str
    price: float
    description: str
    image: str
    country: str
    
    
class UpdateProductRequest(BaseModel):
    name: str | None = None
    quantity: int | None = None
    price: float | None = None
    description: str | None = None
    image: str | None = None
    country: str | None = None