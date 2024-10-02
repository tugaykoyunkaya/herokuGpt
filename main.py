import flask
import os
from flask import Flask, jsonify
from pytube import YouTube
import logging

app = flask.Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/download')
def download_route():
    try:
        logger.info("Starting video download")
        yt = YouTube("https://www.youtube.com/watch?v=n0fW88BMBno")
        ys = yt.streams.filter(res="360p").first().download()
        logger.info("Video downloaded successfully")
        return jsonify({"success": True, "message": "Video downloaded successfully"})
    except Exception as e:
        logger.error(f"Download error: {str(e)}")
        return jsonify({"success": False, "message": "Download error"})

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()