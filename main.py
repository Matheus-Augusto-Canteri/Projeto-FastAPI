from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_languages():
    return {"success" : "funcionou"}