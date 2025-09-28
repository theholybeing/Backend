import requests
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

API_KEY = "dc6f8240b997f5fb0a077654a694044e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/weather/{city}")
async def get_weather(city: str):

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="City not found or API error.")

    data = response.json()
    
    try:
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return {
            "city": data["name"],
            "temperature": f"{temp}°C",
            "description": description.title()
        }
    except KeyError:
        raise HTTPException(status_code=500, detail="Error parsing weather data.")