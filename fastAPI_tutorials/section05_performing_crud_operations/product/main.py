from fastapi import FastAPI, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from product import models, schemas
from schemas import Product
from models import Product
from typing import List
from database import Base, engine, SessionLocal, get_db
from hashed_password import pwd_context

app = FastAPI(
    title ="product API",
    description="get details for all the product on the website.",
    terms_of_service="http://www.google.com",
    contact={
        "developer" : "Gopalakrishna",
        "website" : "http://ww.gk.com",
        "email": "gkrm@gmail.com",
        "licence_info" : "None"
    },
    docs_url='/pubsub/v1/admin/docs#/',redoc_url=None
)

models.Base.metadata.create_all(engine)


@app.post('/product', status_code=status.HTTP_201_CREATED,tags =['product'])
def add(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(
        name=Product.name,
        description=Product.description,
        price=Product.price
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.post('/seller',response_model= schemas.DisplaySeller,tags =['seller'])
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    # hashed_password = pwd_context.hash(request.password)
    new_seller = models.Seller(
        username=request.username,
        email=request.email,
        password=pwd_context.hash(request.password)  # hashed the password.
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller


# response_model= schemas.DisplayProduct --> response body formatted in own way.
@app.get('/products', response_model=List[schemas.DisplayProduct],tags =['product'])
def products_get_all(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products


# response_model= schemas.DisplayProduct --> response body formatted in own way.
@app.get('/products/{id}', response_model=schemas.DisplayProduct,tags =['product'])
def product_get(id, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail='product not found')
    return product


@app.delete('/products/{id}',tags =['product'])
def product_delete(id, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='product not found')

    db.commit()
    return {"product is deleted : ": {product}}


@app.put('/products/{id}',tags =['product'])
def product(request: schemas.Product, id, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product:
        pass
    product.update(request.dicts())
    db.commit()
    return {"product is successfully updated ": {product}}


"""
@app.post('/product',status_code =200) or @app.post('/product',status_code=status.HTTP_201_CREATED)---> if at all wanted to mention expected status code explicitly the use this way.   
"""
