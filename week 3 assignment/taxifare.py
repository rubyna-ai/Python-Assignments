trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

for trip in trips:
    distance = trip["distance"]
    hour = trip["hour"]
    fare = 150
    if distance > 2 and distance <= 10:
        fare = fare + (distance - 2) * 35
    if distance > 10:
        fare = fare + (8 * 35)
        fare = fare + (distance - 10) * 28
    if hour >= 22 or hour < 5:
        fare = fare + (fare * 0.10)
        time = "Night"
    else:
        time = "Day"
    print(f"Distance: {distance}km | Time: {time} | Fare: NPR {fare}")