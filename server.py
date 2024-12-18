'''Server for a flask based web application that analyzes the emotions
   in a user inputted text.'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    '''Analyzes the emotion in a user inputted text via the Watson NLP Library
       and returns a formatted string containing a summary of the analysis'''
    text_to_analyze = request.args.get("textToAnalyze")
    resp = emotion_detector(text_to_analyze)

    if resp["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is 'anger': {resp['anger']}, "
            f"'disgust': {resp['disgust']}, 'fear': {resp['fear']}, 'joy': {resp['joy']}"
            f", and 'sadness': {resp['sadness']}. The dominant emotion is "
            f"{resp['dominant_emotion']}.")

@app.route("/")
def index():
    '''Renders the index page for the web application.'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
