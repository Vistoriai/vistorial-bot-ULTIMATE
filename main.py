from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os

app = FastAPI()

@app.get("/")
async def root():
    return JSONResponse({"status": "ONLINE"})

@app.post("/webhook")
async def webhook(request: Request):
    return JSONResponse({"success": True})
