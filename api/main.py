from mangum import Mangum
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import urllib.parse
import requests
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")
API_KEY = os.environ.get("API_KEY")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})


@app.get("/stocks/{symbol}", response_class=HTMLResponse)
async def get_name(request: Request, symbol: str):
    url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    quote = response.json()
    info = {"name": quote["companyName"],
    "price": float(quote["latestPrice"]),
    "symbol": quote["symbol"]
    }
    return templates.TemplateResponse("hello.html", {"request": request, "company_name": info["name"], "price": info["price"]})

handler = Mangum(app=app)
