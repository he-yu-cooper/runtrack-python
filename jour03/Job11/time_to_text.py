def time_to_text(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    print(f"{hours}h{remaining_minutes}min")

time_to_text(150) 
time_to_text(25)  
time_to_text(300)

