import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker version 2.o")
    while True:
        x = input("Enter what you want the system to speak: ")
        if x=="q":
            engine = pyttsx3.init()
            engine.say("BYE-BYE Friend !!")
            engine.runAndWait()
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()