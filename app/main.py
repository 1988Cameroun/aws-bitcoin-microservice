from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.aws_client import list_s3_buckets
from app.bitcoin_client import get_bitcoin_blockchain_info

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "AWS + Bitcoin microservice running"}

@app.get("/aws/s3")
async def aws_s3_buckets():
    buckets = list_s3_buckets()
    return {"buckets": buckets}

@app.get("/bitcoin/blockchaininfo")
async def bitcoin_info():
    info = get_bitcoin_blockchain_info()
    return info