from fastapi import FastAPI, HTTPException

app = FastAPI()

# Istniejący endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, Bait Boat!"}

# Endpoint do sterowania ruchem łódki
@app.post("/move/")
def move_boat(direction: str):
    if direction not in ["forward", "backward", "left", "right"]:
        raise HTTPException(status_code=400, detail="Invalid direction")
    # Logika sterowania łódką
    # To jest miejsce, gdzie dodasz integrację z faktycznym systemem łódki
    return {"status": "success", "direction": direction}

@app.get("/battery/")
def check_battery():
    battery_level = 85  # Przykładowa wartość, później pobierana z urządzenia
    return {"battery_level": battery_level}

@app.get("/range/")
def check_range():
    range_status = "in range"  # Przykładowa wartość
    return {"range_status": range_status}

@app.post("/return/")
def auto_return():
    # Symulacja operacji powrotu do punktu startowego
    return {"status": "success", "message": "Boat is returning to start point"}
