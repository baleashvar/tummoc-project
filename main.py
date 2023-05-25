from typing import Dict
from fastapi import FastAPI

app = FastAPI()

candidates = ["John", "Jane", "Jack"]
votes = {candidate: 0 for candidate in candidates}

@app.get("/vote/{name}")
async def vote(name: str) -> Dict[str, int]:
    if name in candidates:
        votes[name] += 1
        return {"success": True}
    else:
        return {"success": False}

@app.get("/winner")
async def print_winner() -> str:
    max_votes = max(votes.values())
    winners = [candidate for candidate, vote in votes.items() if vote == max_votes]
    if len(winners) == 1:
        return winners[0]
    else:
        return "\n".join(winners)

