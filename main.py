from fastapi import FastAPI, Form
import uvicorn
from mailer import send_mail

app = FastAPI(title='Mail API')

@app.get('/')
def index():
    return {'message':'FastAPI Mail'}

@app.post('/mail')
async def mail(to = Form(), subject = Form(), body = Form()):
    await send_mail(to=to, subject=subject, body=body)
    return {'message':'done'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=5000)