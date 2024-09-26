import speech_recognition as sr
import webbrowser
import pyttsx3  # text to speech module
import sys  # To exit the program

recognizer = sr.Recognizer()  # speech recognition functionality enabled
engine = pyttsx3.init()  # pyttsx initialized

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    print(f"Processing command: {command}")
    
    # Command matching
    if 'open google' in command.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif 'open youtube' in command.lower():
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif 'open Notion' in command.lower():
        speak("Opening Notion")
        webbrowser.open("https://Notion.com")
    elif 'open linkedin' in command.lower():
        speak("Opening Linkedin")
        webbrowser.open("https://linkedin.com")
    elif 'thanks' in command.lower():
        speak("You're welcome! Shutting down.")
        sys.exit()  # Close the program
    else:
        speak("Command not recognized")

def listen_for_command():
    # Continuous listening after Alfred is activated
    with sr.Microphone() as source:
        print("Listening for command.....")
        recognizer.adjust_for_ambient_noise(source)  # Adjust mic for background noise
        audio = recognizer.listen(source, timeout=20, phrase_time_limit=10)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized command: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

if __name__ == '__main__':
    speak("Initializing ALFRED.....")
    
    while True:
        try:
            # Listening for wake word first
            with sr.Microphone() as source:
                print("Listening.....")
                recognizer.adjust_for_ambient_noise(source)  # Adjust mic for background noise
                audio = recognizer.listen(source, timeout=20, phrase_time_limit=10)  # Faster response time
            
            word = recognizer.recognize_google(audio)
            print(f"Recognized word: {word}")  # Debugging line to check wake word
            
            if word.lower() == "alfred":
                speak('On your service')
                
                # Continuous command loop after activation
                while True:
                    command = listen_for_command()
                    if command:
                        processCommand(command)  # Pass the recognized command to process
         
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")
