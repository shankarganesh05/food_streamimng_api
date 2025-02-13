from fastapi import FastAPI, Request
import json
import uvicorn

app=FastAPI()

@app.post('/post_data')
def post_data():
    message = Request.json
    return message

if __name__ == '__main__':
    uvicorn.run(app, port=5000, host='0.0.0.0')
