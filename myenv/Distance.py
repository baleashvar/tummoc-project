from fastapi import FastAPI
from geopy import distance

app = FastAPI()

@app.post("/distance")
def get_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    """
    Get the distance between two points in latitude and longitude.

    Args:
        lat1: The latitude of the first point.
        lon1: The longitude of the first point.
        lat2: The latitude of the second point.
        lon2: The longitude of the second point.

    Returns:
        The distance between the two points in kilometers.
    """

    distance_in_km = distance.distance((lat1, lon1), (lat2, lon2)).kilometers
    return distance_in_km

if __name__ == "__main__":
    app.run()
