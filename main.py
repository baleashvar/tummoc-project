from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/wap")
def wap_endpoint():
    return {"message": "This is the WAP endpoint!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)