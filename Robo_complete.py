import pyttsx3
import Robo

if __name__ == '__main__':
 b = Robo.heading()   # It is a user building function created by me it is comming from main file Robo.py


 while True:
    engine = pyttsx3.init()
    print()
    bc = input("Enter Your Statement: ")
    engine.setProperty('rate', 150)
    engine.say(bc)
    engine.runAndWait()

    if  bc == 'q':
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            dc= "Bye Bye Friends Thank You For Using me"
            print("Bye Bye Friends Thank You For Using Me...")
            engine.say(dc)
            engine.runAndWait()
            break


        
