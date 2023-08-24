''' This main server file initiates the application of emotion detection
    to be executed over the Flask channel and deployed on localhost:5000.
'''

# various necessary imports
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
# initiating the flask app
app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_detect():
    ''' This emotion_detect() function receives the entered text from
        the HTML interface and runs emotion detection analysis over it using
        the imported emotion_detector() function. The output returned gives
        the system's determination of the levels of emotions present in the
        text along with the text's dominant emotion.
    '''

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['anger'] is None:
        return "<b>Invalid text! Please try again!</b>"

    intro = "For the given statement, the system response is "
    outro = " The dominant emotion is "
    anger = f"'anger': {response['anger']}"
    disgust = f"'disgust': {response['disgust']}"
    fear = f"'fear': {response['fear']}"
    joy = f"'joy': {response['joy']}"
    sadness = f"'sadness': {response['sadness']}"
    dominant = f"<b>{response['dominant_emotion']}</b>"
    return f"{intro}{anger}, {disgust}, {fear}, {joy}, and {sadness}.{outro}{dominant}."

@app.route('/')
def render_index_page():
    ''' This render_index_page() function initiates the rendering of the main
        application page over the Flask channel.
    '''

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
