from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def calculate_grade(final_score: float):
    if final_score > 85:
        return "A"
    elif 75 < final_score <= 85:
        return "AB"
    elif 65 < final_score <= 75:
        return "B"
    elif 60 < final_score <= 65:
        return "BC"
    elif 50 < final_score <= 60:
        return "C"
    elif 40 < final_score <= 50:
        return "D"
    else:
        return "E"


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    praktikum: float = Form(...),
    tugas_besar: float = Form(...),
    tugas: float = Form(...),
    quiz: float = Form(...),
    uts: float = Form(...),
    uas: float = Form(...)
):

    final_score = (
        praktikum * 0.20 +
        tugas_besar * 0.10 +
        tugas * 0.10 +
        quiz * 0.10 +
        uts * 0.25 +
        uas * 0.25
    )

    grade = calculate_grade(final_score)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "final_score": round(final_score, 2),
        "grade": grade
    })

import os

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)

