from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "루트 페이지임."

