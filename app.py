from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return{"status": "Mail Server is Running!!!"}


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', reload=True)