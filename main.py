from fastapi import FastAPI
app = FastAPI

@app.get("/welcome")
def welcome():
    return{
        "massage":"hello and welcome"
    }

