from fastapi import FastAPI

app = FastAPI()


# コードは適当
@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}
