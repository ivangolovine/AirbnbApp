from API.googleTest import *
from API.connectDB import *
from interfaceGUI import DisplayInterface

def main():
    try:
        DisplayInterface()
        #login_Airbnb_bs4()
        #login_Airbnb()
        #print("Try statement")
    except Exception as err:
        print("Error Parsing", err)
 
if __name__ == "__main__":
    main()