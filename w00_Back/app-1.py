from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
import datetime
import bcrypt
import jwt
import pathlib
import textwrap
import os
import google.generativeai as genai
import PIL.Image
import base64
from io import BytesIO
from models import imgToStoryData
import hashlib

genai.configure(api_key="AIzaSyCGrmdSBF64WiIa8nEg_uLmHsMyZ4ateYI")
client = MongoClient("localhost", 27017)

db = client.JamTalk

app = Flask(__name__)

# app.config["SECRET_KEY"] = os.urandom(24)
SECRET_KEY = 'Jungle'

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    # 클라이언트로부터 받은 이메일과 비밀번호
    userId = request.form["userId"]
    password = request.form["password"]

    pw_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

    payload = {
        "id": userId,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=100),
    }
    # 사용자 인증
    if userId == "hello" and password == "world":
        # JWT 토큰 생성
        payload = {
            "id": userId,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=100),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # 클라이언트에게 토큰을 반환
        return jsonify({"result": "success", "token": token})
    else:
        # 로그인 실패 시 에러 메시지 반환
        return jsonify({"error": "로그인 실패"})


storyData = []


# 업로드 페이지 렌더링
@app.route("/upload" ,methods=["POST"])
def upload_page():
    # 클라이언트로부터 전달된 토큰을 가져옴
    token = request.args.get("token")
    if token:
        # 토큰이 존재하는 경우에는 업로드 페이지를 렌더링
        return render_template("upload.html", token=token)
    else:
        # 토큰이 전달되지 않은 경우에는 로그인 페이지로 리다이렉트
        return redirect(url_for("login"))


@app.route("/uploadPhoto", methods=["POST"])
def getPhoto():
    if request.files["file"] is not None:
        file = request.files["file"]
        save_dir = os.path.join(app.root_path, "resources")
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        save_path = os.path.join(save_dir, file.filename)
        file.save(save_path)

        data = imgToStoryData(save_path)
        storyData.extend([data, data, data])
        # return response.text
        return render_template("story.html", storyData=storyData)
    else:
        return jsonify({"error": "No photo uploaded"}), 400


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)
