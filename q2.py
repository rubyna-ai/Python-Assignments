# list of sensors
sensors = [ 
("Chatara", 2.8), 
("Tribeni Ghat", 5.4), 
("Koshi Barrage", 4.1), 
("Sunsari Bridge", 1.9), 
("Saptakoshi Camp", 6.0), 
] 

def check_water_level(location, level_metres):
    # below 3 metres — safe
    if level_metres < 3:
        return "Safe"
    
    # between 3 and 5 metres — warning
    elif level_metres <= 5:
        return "Warning — Alert nearby villages"
    
    # above 5 metres — danger
    else:
        return "DANGER — Evacuate immediately!"

# loop through each sensor and print the result
for location, level in sensors:
    status = check_water_level(location, level)
    print(f"{location} ({level} m): {status}")