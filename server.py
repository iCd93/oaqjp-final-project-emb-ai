"""Flask server that exposes the emotion detection application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Run emotion detection on the text provided via query parameter.

    Reads 'textToAnalyze' from the request arguments, runs the
    emotion_detector function on it, and returns a formatted string
    with the scores for each emotion and the dominant emotion. If the
    input text is invalid or blank, returns an error message instead.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render and return the main index page of the application."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
