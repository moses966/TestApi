from fastapi import FastAPI
from .testing import get_greeting

app = FastAPI()

@app.get("/greeting")
def read_greeting():
    greeting = get_greeting()
    if greeting:
        return {"greeting": greeting}
    else:
        return {"error": "Unable to fetch greeting"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
