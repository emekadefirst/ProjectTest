from sessions import *
from schemas import *
from pathlib import Path
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, File, UploadFile, Form

UPLOAD_DIR = Path("uploaded_images")
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/product/all")
def all():
    data = all_product()
    return data

@app.get("/product/{id}")
async def get(id):
    product = await get_by_id(id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/product/")
async def create_product(
    name: str = Form(...),
    quantity: int = Form(...),
    price: float = Form(...),
    description: str = Form(...),
    image: UploadFile = File(...),
    country: str = Form(...)
):
    # Save the uploaded image
    file_path = UPLOAD_DIR / image.filename
    with file_path.open("wb") as f:
        f.write(await image.read())
    result = add_product(name, quantity, price, description, str(file_path), country)
    return JSONResponse(content={"message": result})

@app.post("/products/search")
async def search_products_api(search_product: SearchProduct):
    results = search_products(search_product.query)
    if not results:
        raise HTTPException(status_code=404, detail="No products found")
    return results

@app.put("/product/update/{id}")
async def update(id: int, product_update: UpdateProductRequest):
    product = update_product(
        product_id=id,
        name=product_update.name,
        quantity=product_update.quantity,
        price=product_update.price,
        description=product_update.description,
        image=product_update.image,
        country=product_update.country
    )
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.delete("/product/delete/{id}")
async def delete(id: int):
    product = delete_product(id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}