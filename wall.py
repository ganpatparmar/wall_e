# wall_e
# Python program   to read
# json file


import json
import pyttsx3
import schedule
from datetime import datetime


now = datetime.now()
time = now.strftime("%H%M")

print(time)
print(type(time))

time2=int(time)
print(type(time2))
time3= time2-2
print(time3)
time4=str(time3)
print(type(time4))


engine = pyttsx3.init()

# Opening JSON file
f = open('schedule.json',)

# returns JSON object as
# a dictionary
data = json.load(f)
jsonData = data["time"]


for x in jsonData:
    keys = x.keys()
    print(keys)
    print(type(keys))
    newd = str(keys)
    print(newd)
    print(type(newd))
    newd1=str(newd)

if newd1 == time4:
       print(data)  
    

    

# Iterating through the json
# list

#example code
#dct = {
 #    "1": "a",
  #   "3": "b",
   #"8": {
    #   "12": "c",
     #    "25": "d"
 #}
 #}

#key=dct.keys()
#print(key)
#print(type(key))
#key2= str(key)
#print(type(key2))

#example2 code

        
        
# Driver code    
#y = data['1410']



#for i in [time3 == y]:
 #   engine.say(i)
   # engine.runAndWait()
   # print("current time",time)
	

# Closing file

f.close()

