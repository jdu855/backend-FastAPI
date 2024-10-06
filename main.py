from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
def read_root():
    return {"nombre": "Juan David Rodriguez"}

@app.get("/users")
def list_users():
    return[
        {
            'name': 'juan david rodriguez',
            'email': 'juanrod@gmail.com'
        },
        {
            'name': 'lady sanches',
            'email': 'sancheslady@gmail.com'
        }
    ]