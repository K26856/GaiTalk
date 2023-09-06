from pprint import pprint
from text2speech import Text2Speech, VoicevoxWrapper
from aitalk import AiTalk, MiiboWrapper
from flask import Flask, request, make_response, jsonify

import os
import json

# app initiate
with open('./config/settings.json', mode='r', encoding='utf-8') as f :
    config = json.load(f)
app = Flask(__name__)
text2speeches = {
    "voicevox" : VoicevoxWrapper()
}
aitalks = {
    "miibo" : MiiboWrapper(api_key=config['aitalk']['miibo']['api_key'], agent_id=config['aitalk']['miibo']['agent_id'])
}


# route
@app.route("/", methods=["GET"])
def index() :
    return "Hello world"


# text2speech
@app.route("/text2speech/models", methods=["GET"])
def get_text2speech_models() :
    result = [key for key in text2speeches.keys()]
    response = make_response(json.dumps(result, ensure_ascii=False), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route("/text2speech/speakers", methods=["GET"])
def get_text2speech_speakers() :
    req = request.args
    model = req.get("model")
    result = text2speeches[model].get_speaker_ids()
    response = make_response(json.dumps(result, ensure_ascii=False), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route("/text2speech/tts", methods=["POST"])
def get_text2speech_tts() :
    model = request.form["model"]
    speaker_id = request.form["speaker_id"]
    text = request.form["text"]
    print("{}, {}, {}".format(model, speaker_id, text))
    result = text2speeches[model].tts(text, int(speaker_id))
    response = make_response(result, 200)
    response.headers['Content-Type'] = 'audio/wav'
    response.headers['Content-Disposition'] = 'attachment; filename=sound.wav'
    return response


# aitalk
@app.route("/aitalk/models", methods=["GET"])
def get_aitalk_models() :
    result = [key for key in aitalks.keys()]
    response = make_response(json.dumps(result, ensure_ascii=False), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route("/aitalk/reply", methods=["POST"])
def get_aitalk_reply() :
    model = request.form["model"]
    text = request.form["text"]
    uid = request.form["uid"]
    print("{}, {}, {}".format(model, text, uid))
    result = {}
    result['response'] = aitalks[model].send(text, uid)
    response = make_response(json.dumps(result, ensure_ascii=False), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == "__main__" :
    app.run(port=8888)