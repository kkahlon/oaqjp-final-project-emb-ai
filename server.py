from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def RunSentimentAnalysis():
    text_to_analyze = request.args.get("textToAnalyze")
    resp = emotion_detector(text_to_analyze)

    return (f"For the given statement, the system response is 'anger': {resp['anger']}, "
            f"'disgust': {resp['disgust']}, 'fear': {resp['fear']}, 'joy': {resp['joy']}"
            f", and 'sadness': {resp['sadness']}. The dominant emotion is {resp['dominant_emotion']}.")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)