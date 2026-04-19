for h in range(24):
    if h ==0:suffix="12 midnight"
    elif h==12:suffix="12 noon"
    elif h<12:suffix=f"{h} AM"
    else: suffix =f"{h-12} PM"
    print(suffix)
    
