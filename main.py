from fastapi import FastAPI

app = FastAPI()

class Election:
    def __init__(self):
        self.candidates = {}
    
    def vote(self, name):
        if name in self.candidates:
            self.candidates[name] += 1
            return True
        else:
            return False
    
    def get_winner(self):
        max_votes = max(self.candidates.values())
        winners = [candidate for candidate, votes in self.candidates.items() if votes == max_votes]
        return winners


election = Election()

@app.post("/vote/{candidate}")
def vote(candidate: str):
    if election.vote(candidate):
        return {"message": "Vote successful"}
    else:
        return {"message": "Invalid ballot"}

@app.get("/winner")
def get_winner():
    winners = election.get_winner()
    return {"winners": winners}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)