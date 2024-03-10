from fastapi import FastAPI, BackgroundTasks
from config import MailBody
from mailer import send_mail
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return{"status": "Mail Server is Running!!!"}


@app.post("/send_mail")
async def schedule_mail(req:MailBody, tasks:BackgroundTasks):
    data = req.dict()
    tasks.add_task(send_mail, data)
    return {"status": 200, "message": "Mail Scheduled Successfully"}


if __name__ == "__main__":
    uvicorn.run('app:app', host='127.0.0.1', reload=True)