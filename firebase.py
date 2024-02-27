# Imports
#-------------------------------------------------------------------------------
import pyrebase

# Config/Setup
#-------------------------------------------------------------------------------
firebaseConfig = {
  "apiKey":"AIzaSyA679YbOQ86DXu6I86UK2un9dZ6_S0QmeE",
  "authDomain": "thirdeye-88d12.firebaseapp.com",
  "projectId": "thirdeye-88d12",
  "storageBucket": "thirdeye-88d12.appspot.com",
  "messagingSenderId": "102399511344",
  "appId": "1:102399511344:web:7240e22b08101bc3d256f5",
  "measurementId": "G-THN1Z0MN8M",
  "databaseURL": "https://thirdeye-88d12-default-rtdb.firebaseio.com/"
  };
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def name(data1):
    data = {"Name":f"{data1}"}
    #-------------------------------------------------------------------------------
    # Create Data

    db.child("data").child("01").set(data)
    print("done")
