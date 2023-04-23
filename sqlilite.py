import cv2
import pytesseract
import datetime
import sqlite3

pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR"  # type: ignore

# Initialize the database
conn = sqlite3.connect('car_plate.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS car_plate 
             (sr_no INTEGER PRIMARY KEY,
              in_time TEXT NOT NULL,
              car_numberplate TEXT NOT NULL)''')

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Initialize a set to store the license plates that have already entered the database
existing_plates = set()

while True:
    # Read frame from camera
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to grayscale and apply thresholding to get a binary image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    # Perform OCR on the binary image to get the license plate text
    plate_text = pytesseract.image_to_string(threshold_img, config='--psm 11')
    
    # If a license plate is detected, save the car number and entry time to the database
    if plate_text and plate_text not in existing_plates:
        now = datetime.datetime.now()
        in_time = now.strftime("%Y-%m-%d %H:%M:%S")
        car_numberplate = plate_text.strip()
        
        # Check if this car has already entered the database
        c.execute("SELECT * FROM car_plate WHERE car_numberplate=?", (car_numberplate,))
        existing_entry = c.fetchone()
        if existing_entry is None:
            # If the car has not already entered the database, insert a new entry
            c.execute("INSERT INTO car_plate (in_time, car_numberplate) VALUES (?, ?)", (in_time,car_numberplate))
            conn.commit()
            existing_plates.add(car_numberplate)
            print(f"New entry added to database: {in_time}- {car_numberplate}")
    
    # Display the frame and the detected license plate text
    cv2.imshow('Number Plate', frame)
    print(f"Detected license plate: {plate_text}")
    
    # Press Q to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()
conn.close()
