import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.templating import Jinja2Templates
import uvicorn
import requests
from Dash_app import app as app_dash

# creer l'objet de FastApi
app = FastAPI()

# Obtenir le chemin absolu vers le repertoire des modeles
templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'templates'))

# Obtenir le chemin absolu vers le repertoire des modeles
stactic_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'static'))

# configurer le modele Jinja2 pour le rendu des fichiers HTML
templates = Jinja2Templates(directory=templates_dir)


#fichier static
app.mount("/static",StaticFiles(directory=stactic_dir))

# Monter l'application Dash sours chemin / Dashbaoard
app.mount("/dashboard", WSGIMiddleware(app_dash.server))



user = {"admin":"123"}

EXTERNAL_API_URL = "http://127.0.0.1:8000/info"

def get_external_info():
    try:
        response = requests.get(EXTERNAL_API_URL)
        return response.json()
    
    except Exception as e:
        return {
            "date":"N/A",
            "time":"N/A",
            "weather":{
                "city":"N/A",
                "temperature":"N/A",
                "description":"N/A"
            } 
    }

@app.get("/api/info")
async def get_info():
    info = get_external_info()
    return info

@app.get("/")
async def home_page(request:Request):
    info = get_external_info()
    return templates.TemplateResponse('home.html', {"request":request,'info':info})

@app.get("/login")
async def login_page(request:Request):
    return templates.TemplateResponse('login.html',{"request":request})

@app.post("/login")
async def login(request : Request , username:str = Form(...), password: str = Form(...)):
    if username in user and user[username] ==password:
        response = RedirectResponse(url='/dashboard', status_code=302)
        response.set_cookie(key="Authorization", value="Bearer Token" , httponly=True)
        return response
    return templates.TemplateResponse("login.html",{"request":request , "error":"Invalid username and password"})

@app.get("/logout")
async def logout():
    response = RedirectResponse(url='/login')
    response.delete_cookie('Authorization')
    return response