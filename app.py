from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/')
def sentiment_analysis():
    return {
        "hello": "world"
    }