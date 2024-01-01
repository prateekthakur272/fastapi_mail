from fastapi import FastAPI
import uvicorn

app = FastAPI(title='Mail API')

@app.get('/')
def index():
    return {'message':'FastAPI Mail'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=5000)