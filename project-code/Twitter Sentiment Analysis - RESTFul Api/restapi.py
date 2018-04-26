from flask import Flask, jsonify, request, render_template, session, redirect, url_for, send_file
import twitter_analysis_with_sparkobj as ta
import cloud_computing_project as tg
import os

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
app = Flask(__name__)

@app.route('/')
def index():
    path=app.config.get('STATIC_FOLDER')
    return render_template("main.html")


@app.route('/search_word', methods=['POST'])
def search_word():
    word = request.form['Search']
    for file in os.scandir("static/"):
        os.unlink(file.path)
    tg.twitter_download(word)
    ta.start_spark_sentiment_analysis(word)
    return render_template("result.html")



if __name__ == '__main__':
    app.run(debug=True)
