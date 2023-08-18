from cvzone.HandTrackingModule import HandDetector
import cv2
import pyttsx3
import time
import pywhatkit
import random as rdm

def coffeeMaker():
    model = HandDetector()

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[1].id)

    cap = cv2.VideoCapture(0)

    music_list = ['hawayein ', 'jab koi baat', 'senorita', 'calm down', 'dheere dheere se meri zindagi',
                  'hamsafar', 'lollipop lagelu']

    pyttsx3.speak("Good Evening")

    while True:
        try:
            status, photo = cap.read()
            cv2.imshow("hi", photo)

            if cv2.waitKey(100) == 13:
                break

            # Initialize flag outside the loop
            flag = 0

            hand = model.findHands(photo, draw=False)
            if hand:
                lmlist = hand[0]
                fingeruplist = model.fingersUp(lmlist)
                print(fingeruplist)
                
                if fingeruplist is not None:
                    if flag == 0:
                        pyttsx3.speak("Welcome to the Coffee shop, Tell me the quantity you want?")
                        flag = 1  # Increment flag directly

                    time.sleep(2)
                
                if fingeruplist == [0, 1, 0, 0, 0]:
                    pyttsx3.speak("Your single coffee is preparing. Please wait for 10 minutes.")
                    pyttsx3.speak("Let's have some music")
                    
                    # Play music
                    music_selected = rdm.choice(music_list)
                    pywhatkit.playonyt(music_selected)
                    time.sleep(1)
                
                elif fingeruplist == [0, 1, 1, 0, 0]:
                    pyttsx3.speak("We are preparing two coffees for you. Please wait. Have a great day.")
                    pyttsx3.speak("If you want to listen to some music, show me the okay sign.")
                    
                    # Play music
                    music_selected = rdm.choice(music_list)
                    pywhatkit.playonyt(music_selected)
                    time.sleep(1)
                
                elif fingeruplist == [0, 1, 1, 1, 0]:
                    pyttsx3.speak("We are preparing three coffees for you. Please wait. Have a great day.")

                else:
                    pass
                
                # Reset fingeruplist to None after processing
                fingeruplist = None

        except Exception as e:
            print("Exception:", e)

    cv2.destroyAllWindows()
    cap.release()

coffeeMaker()
