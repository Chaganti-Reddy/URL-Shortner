from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random, string

app = FastAPI()
url_db = {}

class URLRequest(BaseModel):
    original_url: str

@app.post("/shorten")
def shorten_url(request: URLRequest):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url_db[code] = request.original_url
    return {"short_url": f"http://localhost:8000/{code}"}

@app.get("/{code}")
def redirect(code: str):
    url = url_db.get(code)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"redirect_to": url}
