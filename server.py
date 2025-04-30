''' Import flask modules and emotion detection package
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' Route to analyze text and return emotion prediction
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyse)
    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted = f"For the given statement, the system response is 'anger': \
    {res['anger']}, 'disgust': {res['disgust']}, 'fear': {res['fear']}, 'joy': {res['joy']}, \
    'sadness': {res['sadness']}. The dominant emotion is <b>{res['dominant_emotion']}</b>"
    return formatted

@app.route("/")
def render_index_page():
    ''' Route to return templated page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
