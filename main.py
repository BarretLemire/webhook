from fastapi import FastAPI, Request




app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "Hello World!"}

@app.post("/webhook")
async def webhook(request: Request):
    return {"message": "webhook recieved"}