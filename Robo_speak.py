import pyttsx3
import time

if __name__ == "__main__":
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  
    engine.say("Welcome To Robo Speak 12.3 Developed By Mr. Alex...")
    engine.runAndWait()
    time.sleep(2)
    print()

    print("                  Welcome To Robo Speak 12.3 Developed By Mr. Alex...")
    print("             ______________________________________________________________")
    time.sleep(3)
    while True:

        engine = pyttsx3.init()

    # Get input from the user
        print()
        bc = input("Enter Your Statement: ")

    # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech

    # Speak the user input
        engine.say(bc)

    # Wait for the speech to finish
        engine.runAndWait()

        if bc == 'y':
            break

       
