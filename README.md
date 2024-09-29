
# Alfred: Your Personal AI Assistant

Alfred is a voice-activated AI assistant that can open various applications, provide time, date, device location, weather forecasts, and deliver task reports in both speaking and writing formats. Alfred can open Google, YouTube, LinkedIn, and Notion, making it a versatile tool for boosting your productivity.




## Features

- Open Applications:
  - Google
  - Youtube
  - Linkedin
  - Notion
- Real Date & Time Update
- Device Location Status
- Weather Forcast
- Task Report Status


## Installation

Step-1: Clone the repository: 

```bash
git clone https://github.com/aimG313/Personal-Ai-Assistant--ALFRED.git
cd Personal-Ai-Assistant--ALFRED
```

Step-2: Install the necessary dependencies:

- Use the following command to install the required packages:

```bash
pip install -r requirements.txt
```
Step-3: Set up API keys (for weather, location, etc.):

- Add your API keys to the .env file for services like weather forecast and location tracking.

Step-4: Run Alfred:

- Start Alfred by running:

```bash
python main.py
```



    
## Usage

- Simply speak or type commands, such as:
  - "Open Google"
  - "What's the weather?"
  - "Give me the task report for today"
  
Alfred will respond accordingly, either by opening the requested app, giving you information, or providing you with a spoken and written report.


## Technology Used

**Python:** Core language for development

**SpeechRecognition:** For voice inputs

**Requests:** For fetching weather data

**Geopy:** For getting device location

**Audiopy:** For speech output

## Future Improvement Plans

- Add more applications to be controlled via voice.
- Enhance Alfred's conversational abilities using NLP models.
- Integration with additional productivity tools like Trello, Slack, etc.
## Acknowledgements

 - [Ip-Api Key](https://ipapi.com/)
 - [Open Weather API](https://openweathermap.org/api)
 - [Geopy](https://geopy.readthedocs.io/en/stable/)


## Contributing

Contributions are always welcome!

Feel free to contribute by opening an issue or submitting a pull request. For major changes, please open an issue first to discuss what you'd like to change.
## Contact:

If you have any questions or feedback, feel free to reach out via email at: ashrafulmahi313@gmail.com