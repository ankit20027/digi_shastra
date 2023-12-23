# from fastapi import FastAPI
# from pydantic import BaseModel, Field
# from uuid import UUID
# import sqlalchemy

# app = FastAPI()

# class GeetaShloks(BaseModel):
#     id: UUID
#     chapter:int = Field(ge=1, le=18)
#     verse:int = Field(ge=1)
#     shloka:str = Field(min_length=1)
#     hindi:str = Field(min_length=1)
#     english:str = Field(min_length=1)

# @app.get('/')
# def main():
#     return {"Hello": "maa"}
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}