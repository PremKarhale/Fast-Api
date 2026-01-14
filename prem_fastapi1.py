from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional 

app=FastAPI()

@app.get("/")
def root():
    return {'message':'hello_world'}

#task 1:update Book

class Bookmodel(BaseModel):
    title:str
    author:str
    price:float

@app.post("/books/{book_id}")

def Create_book(book_id:int,book:Bookmodel,available:Optional[bool]=True):
    return {
    "book_id":book_id,
    "available":available,
    "book":book,
    "message": "Book updated successfully!"
}

#  task 2:user profile

class user_details(BaseModel):
    name:str
    age:int   #pydentic --> used to check the validation
    email:str

@app.post("/users/create")
def get_usr_detail(usr:user_details,send_welcome_email:bool=True):
    if usr.age >=18:
        return {
        "user": {
            "name":usr.name,
            "age":usr.age,
            "email":usr.email
        },
        "send_welcome_email":send_welcome_email,
        "message": "User created successfully!"
        }
    else:
        return {
    "error": "User must be at least 18 years old."
        }
       

# task 3:Order Checkout API

class order_details(BaseModel):
    item_name:str
    quantity:int
    price_per_item:float

@app.post("/orders/{order_id}")
def order_placed(order_id:int,order:order_details,express_delivery:bool=False):
    total = order.quantity * order.price_per_item
    return{
    "order_id":order_id,
    "express_delivery":express_delivery,
    "total_amount": total,
    "order":order,
    "message": "Order placed successfully!"
}