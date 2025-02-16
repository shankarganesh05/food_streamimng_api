from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app=FastAPI()

class Item(BaseModel):
    name: str
    Age: int

@app.post('/post_data')
async   def post_data(item: Item):
    print(item)
    return item

if __name__ == '__main__':
    uvicorn.run(app, port=5000, host='0.0.0.0')
