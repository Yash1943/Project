import datetime
from sqlalchemy import create_engine,text
engine = create_engine('sqlite:///car_plate.db', echo=True)
conn = engine.connect()

s = text("select * from car_plate")

# listdata = conn.execute(s).fetchone()
# license_plate = dict(listdata)['license_plate']
# # vehicle_type = dict(listdata)['vehicle_type']
# entry_time = dict(listdata)['entry_time']
# exit_time = dict(listdata)['exit_time']



hourly_rate = 5
daily_rate = 20

now = datetime.datetime.now()

vehicle_type = input("Enter vehicle type (car/motorcycle/truck): ")
license_plate = input("Enter license plate number: ")
entry_time = input("Enter entry time (in HH:MM format): ")
exit_time = input("Enter exit time (in HH:MM format): ")

entry_time = datetime.datetime.strptime(entry_time, "%H:%M")
exit_time = datetime.datetime.strptime(exit_time, "%H:%M")

parking_duration = (exit_time - entry_time).total_seconds() / 3600
parking_hours = int(parking_duration)
parking_days = parking_hours // 24

if parking_duration <= 1:
    parking_fee = hourly_rate
elif parking_duration <= 24:
    parking_fee = parking_hours * hourly_rate
else:
    parking_fee = parking_days * daily_rate + (parking_hours % 24) * hourly_rate

print("------------------------------")
print("      CAR PARKING RECEIPT     ")
print("------------------------------")
# print("Vehicle type: ", vehicle_type)
print("License plate: ", license_plate)
print("Entry time: ", entry_time.strftime("%H:%M"))
print("Exit time: ", exit_time.strftime("%H:%M"))
print("Parking duration: ", parking_hours, "hours and", (parking_duration - parking_hours) * 60, "minutes")
print("Parking fee: $", parking_fee)
print("------------------------------")