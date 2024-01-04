#tell you that weather the satelight is over your head or not 
#PROJECT ON API USE AND REQUEST CALL 
import requests
from datetime import datetime
import smtplib
import time

my_email = "shubhamtpsingh123@gmail.com"
my_password  = "passshubh@64"

MY_LAT = 21.152451 # Your latitude
MY_LONG = 79.080559 # Your longitude
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #   Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <=iss_latitude <= MY_LAT + 5 and MY_LONG -5<= iss_longitude<=MY_LONG:
        return True
 
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now >= sunset or time_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_iss_overhead()and is_night():
        connection = smtplib.SMTP("smtp.gamil.com")
        connection.starttls()
        connection.login(my_email , my_password)
        connection.sendmail(from_addr= my_email, to_addrs= my_email, msg="subject:LOOK UP👆\n\n the ISS is above you.")
    
    


