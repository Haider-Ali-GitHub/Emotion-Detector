from flask import Flask, request, jsonify, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_api():
    data = request.get_json()
    statement = data.get('text')
    if statement:
        emotions = emotion_detector(statement)
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
            f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} and "
            f"'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."
        )
        return jsonify(response=response_text)
    return jsonify(response="No text provided")

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
