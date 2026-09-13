# Emotion Detection

A small Flask application that analyzes the dominant emotion in text using the Watson emotion detection service.

## Project Structure

```text
final_project/
├── EmotionPredict/
│   └── emotionPredict_analysis.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
└── test_emotion_detection.py
```

## Requirements

- Python 3.10 or later
- Flask
- Requests

Install the dependencies with:

```powershell
python -m pip install flask requests
```

## Run the Application

From the `final_project` directory, run:

```powershell
python server.py
```

Open [http://localhost:5000](http://localhost:5000) in a browser.

## API Example

The analyzer endpoint accepts text through the `textToAnalyze` query parameter:

```text
http://localhost:5000/sentimentAnalyzer?textToAnalyze=I%20am%20glad%20this%20happened
```

Example response:

```text
The given text has been identified as JOY with a score of 0.95.
```

## Run Tests

Run the unit tests from the project directory:

```powershell
python -m unittest test_emotion_detection.py
```

The analyzer requires access to the external Watson service when running against the live API.
