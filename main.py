import speech_recognition as sr
import webbrowser
import pyttsx3
import sys
import datetime
import requests  # For fetching weather data
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function for text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get the current date and time
def get_date_time():
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    speak(f"Current date and time is {date_time}")
    print(f"Current date and time is {date_time}")

# Function to get the device location using ip-api.com
def get_device_location():
    try:
        # Get the device's location using ip-api
        location_url = "http://ip-api.com/json/"
        response = requests.get(location_url)
        location_data = response.json()

        if location_data['status'] == "success":
            city = location_data['city']
            region = location_data['regionName']
            country = location_data['country']
            speak(f"Your device is located in {city}, {region}, {country}.")
            print(f"Your device is located in {city}, {region}, {country}.")
        else:
            speak("Sorry, I am unable to retrieve your location.")
            print("Unable to retrieve location.")
    except Exception as e:
        speak(f"Error retrieving location: {str(e)}")
        print(f"Error retrieving location: {str(e)}")

# Function to get weather using ip-api for geolocation
def get_weather():
    try:
        # Get the current device's geolocation using ip-api
        location_url = "http://ip-api.com/json/"
        location_response = requests.get(location_url)
        location_data = location_response.json()
        
        if location_data['status'] == "success":
            lat = location_data['lat']
            lon = location_data['lon']
            city = location_data['city']
            
            # Use the OpenWeatherMap API to get weather data
            api_key = "##################"  # Replace with your OpenWeatherMap API key
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
            weather_response = requests.get(weather_url)
            weather_data = weather_response.json()

            if weather_data["cod"] == 200:
                temp = weather_data['main']['temp']
                description = weather_data['weather'][0]['description']
                speak(f"The current temperature in {city} is {temp} degrees Celsius with {description}.")
                print(f"The current temperature in {city} is {temp} degrees Celsius with {description}.")
            else:
                speak("Sorry, I couldn't retrieve the weather data.")
                print("Sorry, I couldn't retrieve the weather data.")
        else:
            speak("Sorry, I am unable to retrieve your location for weather data.")
            print("Unable to retrieve location.")
    except Exception as e:
        speak(f"Error in fetching weather: {str(e)}")
        print(f"Error: {str(e)}")

# Function to read and report tasks from task_report.txt
def get_task_report():
    try:
        if os.path.exists("task_report.txt"):
            with open("task_report.txt", "r") as file:
                tasks = file.read()
                if tasks:
                    speak("Here is your task report:")
                    print("Here is your task report:")
                    speak(tasks)
                    print(tasks)
                else:
                    speak("Your task report is empty.")
                    print("Your task report is empty.")
        else:
            speak("Sorry, I couldn't find the task report file.")
            print("Sorry, I couldn't find the task report file.")
    except Exception as e:
        speak("Sorry, there was an error reading the task report.")
        print("Sorry, there was an error reading the task report.")
        print(f"Error: {e}")

# Process commands
def processCommand(command):
    print(f"Processing command: {command}")
    
    if 'open google' in command.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif 'open youtube' in command.lower():
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif 'open notion' in command.lower():
        speak("Opening Notion")
        webbrowser.open("https://notion.com")
    elif 'open linkedin' in command.lower():
        speak("Opening Linkedin")
        webbrowser.open("https://linkedin.com")
    elif 'date and time' in command.lower():
        get_date_time()
    elif 'where am i' in command.lower() or 'device location' in command.lower():
        get_device_location()
    elif 'weather' in command.lower():
        get_weather()
    elif 'task report' in command.lower():
        get_task_report()
    elif 'thanks' in command.lower():
        speak("You're welcome! Shutting down.")
        sys.exit()
    else:
        speak("Command not recognized")

# Listen for command
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command.....")
        recognizer.adjust_for_ambient_noise(source)
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
            with sr.Microphone() as source:
                print("Listening.....")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=20, phrase_time_limit=10)
            
            word = recognizer.recognize_google(audio)
            print(f"Recognized word: {word}")
            
            if word.lower() == "alfred":
                speak('On your service')
                while True:
                    command = listen_for_command()
                    if command:
                        processCommand(command)
         
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")
