"""Flask web application for emotion detection."""

from pathlib import Path

import flask

from EmotionDetection.emotion_detection import emotion_detector


BASE_DIR = Path(__file__).resolve().parent
app = flask.Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)

@app.route("/emotionDetector")
@app.route("/sentimentAnalyzer")
def sent_analyzer() -> str:
    """Analyze request text and return a formatted emotion summary."""
    text_to_analyze = flask.request.args.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return "Invalid input! Please enter some text."

    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return "Invalid input! Please enter some text."

    return f"For the given statement, the system response is {result}."


@app.route("/")
def render_index_page() -> str:
    """Render the emotion detection page."""
    return flask.render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
