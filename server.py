from pathlib import Path
import flask
from EmotionPredict.emotionPredict_analysis import EmotionPredict_analyzer
#Initiate the flask app : TODO
BASE_DIR = Path(__file__).resolve().parent
app = flask.Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = flask.request.args.get('textToAnalyze')
    # Pass the text to the EmotionPredict_analyzer function and store the response
    response = EmotionPredict_analyzer(text_to_analyze)
    # Extract the label and score from the response
    label = response['label']
    score = response['score']
    # Return a formatted string with the emotion label and score
    return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

        

@app.route("/")
def render_index_page():
    return flask.render_template('index.html')

if __name__ == "__main__":
    # Run the Flask app on localhost:5000
    app.run(host="localhost", port=5000)
