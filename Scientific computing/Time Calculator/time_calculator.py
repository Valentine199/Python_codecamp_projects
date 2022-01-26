
def add_time(start, duration, startDay: str = ""):
    # define start time
    startFirst = start.split()
    hour = int(startFirst[0].split(":")[0])
    minute = int(startFirst[0].split(":")[1])

    # Convert it to 24 time format for easier access
    if(startFirst[1] == "PM"):
        hour +=12

    # define duration time
    dHour = int(duration.split(":")[0])
    dMinute = int(duration.split(":")[1])

    NewTime = CalcNewTime(hour, minute, dHour,dMinute)
    newHour = NewTime[0]
    newMin = NewTime[1]
    daysEllapsed = NewTime[2]


    if startDay == "":
        if newHour >= 12:
            newHour -= 12
            if newHour == 0:
                newHour = 12
            answer = f"{newHour}:{newMin} PM"
            if(daysEllapsed>1):
                answer += f" ({daysEllapsed} days later)"
            elif(daysEllapsed == 1):
                answer += f" (next day)"


        else:
            if newHour == 0:
                newHour = 12
            answer = f"{newHour}:{newMin} AM"
            if(daysEllapsed>1):
                answer += f" ({daysEllapsed} days later)"
            elif(daysEllapsed == 1):
                answer += f" (next day)"
    else:
        weekDays = {1 :"Monday", 2: "Tuesday", 3:"Wednesday", 4:"Thursday", 5: "Friday", 6: "Saturday", 7:"Sunday"}
        normalizedDay = startDay.lower().capitalize()

        #I get a list of the keys and select that element which is at the index of the given day
        #then I add the ellapsed days to see how much did it change
        selectedDay = list(weekDays.keys())[list(weekDays.values()).index(normalizedDay)] + daysEllapsed

        while selectedDay > 7:
            selectedDay -= 7
        
        if newHour >= 12:
            newHour -= 12
            if newHour == 0:
                newHour = 12
            answer = f"{newHour}:{newMin} PM, "
            answer += weekDays[selectedDay]
            if daysEllapsed >1 :
                answer += f" ({daysEllapsed} days later)"
            elif(daysEllapsed == 1):
                answer += f" (next day)"


        else:
            if newHour == 0:
                newHour = 12
            answer = f"{newHour}:{newMin} AM, "
            answer += weekDays[selectedDay]
            if daysEllapsed >1 :
                answer += f" ({daysEllapsed} days later)"
            elif(daysEllapsed == 1):
                answer += f" (next day)"
        

    return answer

def CalcNewTime(hour, minute, dHour,dMinute):
    newHour = hour + dHour
    newMin = minute + dMinute
    
    # maximize minutes in 60
    while newMin >= 60:
        newMin -= 60
        newHour +=1
    if newMin <10:
        newMin = '0'+str(newMin)
    
    # calculate days
    daysEllapsed = 0
    while newHour >= 24:
        newHour -= 24
        daysEllapsed +=1

    return newHour, newMin, daysEllapsed
