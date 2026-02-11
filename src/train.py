from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model/model.pkl")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request, G1: float = Form(...), G2: float = Form(...)):
    
    input_df = pd.DataFrame([[G1, G2]], columns=["G1", "G2"])
    prediction = model.predict(input_df)[0]

    return templates.TemplateResponse("index.html", {
        "request": request,
        "prediction": round(float(prediction), 2)
    })
