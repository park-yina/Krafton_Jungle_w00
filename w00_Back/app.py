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

print(jwt.__file__)

genai.configure(api_key="AIzaSyCGrmdSBF64WiIa8nEg_uLmHsMyZ4ateYI")

MONGODB_URI = "mongodb+srv://fixme1537:hellojungle@cluster0.nvitlce.mongodb.net/"
client = MongoClient(MONGODB_URI)
db = client.Jungle
collection = db.Jamtalk

app = Flask(__name__)

# app.config["SECRET_KEY"] = os.urandom(24)
SECRET_KEY = "Jungle"
storyData = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    # 클라이언트로부터 받은 이메일과 비밀번호
    global globalUserId
    data = request.get_json()
    userId = data["userId"]
    password = data["password"]
    globalUserId = userId
    user = collection.find_one({"ID": userId})

    # 사용자 인증
    if userId == user["ID"] and password == user["password"]:
        # JWT 토큰 생성
        payload = {
            "id": userId,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 30),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        # 클라이언트에게 토큰을 반환
        return jsonify({"result": "success", "token": token})
    else:
        # 로그인 실패 시 에러 메시지 반환
        return jsonify({"error": "로그인 실패"})


# 업로드 페이지 렌더링
@app.route("/upload")
def show_upload():
    return render_template("upload.html")


@app.route("/register", methods=["POST"])
def register():
    global globalUserId
    # POST 요청에서 받은 데이터 추출
    user_data = request.form
    user_id = user_data["ID"]
    name = user_data["name"]
    password = user_data["password"]
    globalUserId = user_id
    # 이미 등록된 사용자인지 확인
    if collection.find_one({"ID": user_id}):
        return jsonify({"success": False, "message": "이미 등록된 사용자입니다."}), 400

    # 새 사용자 등록
    user = {
        "ID": user_id,
        "name": name,
        "password": password,  # 보안상의 이유로 비밀번호는 해싱된 값으로 저장해야 합니다.
        "Story": [],
    }
    collection.insert_one(user)

    return jsonify(
        {"success": True, "message": "회원가입이 성공적으로 완료되었습니다."}
    )


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/upload", methods=["POST"])
def getPhoto():
    if request.files["file"] is not None:
        file = request.files["file"]
        save_dir = os.path.join(app.root_path, "resources")
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        save_path = os.path.join(save_dir, file.filename)
        file.save(save_path)

        data = imgToStoryData(save_path)
        storyData.extend([data])

        return redirect(url_for("show_story"))
    else:
        return jsonify({"error": "No photo uploaded"}), 400


@app.route("/story")
def show_story():
    return render_template("story.html", storyData=storyData)


@app.route("/story/save", methods=["POST"])
def saveStory():
    global storyData
    if collection.find_one({"ID": globalUserId}):
        collection.update_one({"ID": globalUserId}, {"$push": {"Story": storyData}})
        storyData = []
        return redirect(url_for("show_upload"))
    else:
        return jsonify({"에러!": "알 수 없는 이유로 저장에 실패하였습니다."}), 400


@app.route("/find")
def find_password():
    return render_template("findPassword.html")


@app.route("/find_result", methods=["POST"])
def find_result():
    user_id = request.form.get("ID")

    user = collection.find_one({"ID": user_id})
    if user:
        password = user["password"]
        return jsonify({"success": True, "password": password})
    else:
        return jsonify({"success": False, "message": "등록된 사용자가 없습니다."}), 404


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)
