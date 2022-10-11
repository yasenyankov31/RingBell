import os 
import datetime
from datetime import date
import calendar

command="mplayer schoolbell_yordan.mp3"

while True:
    my_date = date.today()
    day=calendar.day_name[my_date.weekday()]
    if day!="Sunday" and day!="Saturday":
        now = datetime.datetime.now().strftime('%H:%M')
        print(now,day)
        match now:
            case "07:30":
                os.system(command)
            case "08:10":
                os.system(command)                
            case "08:20":
                os.system(command)
            case "09:00":
                os.system(command)     
            case "09:40":
                os.system(command)
            case "09:50":
                os.system(command)   
            case "10:10":
                os.system(command)  
            case "10:50":
                os.system(command)          
            case "11:00":
                os.system(command) 
            case "11:40":
                os.system(command) 
            case "11:45":
                os.system(command) 
            case "12:25":
                os.system(command) 
            case "12:30":
                os.system(command) 
            case "13:10":
                os.system(command) 
            case "13:20":
                os.system(command) 
            case "14:00":
                os.system(command) 
            case "14:10":
                os.system(command) 
            case "14:50":
                os.system(command) 
            case "15:00":
                os.system(command) 
            case "15:40":
                os.system(command) 
            case "16:00":
                os.system(command) 
            case "16:40":
                os.system(command) 
            case "16:50":
                os.system(command) 
            case "17:30":
                os.system(command) 
            case "17:35":
                os.system(command) 
            case "18:15":
                os.system(command) 
            case "18:20":
                os.system(command) 
            case "19:00":
                os.system(command) 