from flask import Flask, render_template,url_for

app = Flask(__name__, template_folder='../w00_Front/templates')

@app.route('/')
def index():
    dummydata = [
    {
        'story': '나침판이 고장났나',
        'img': 'https://img1.daumcdn.net/thumb/C176x176/?fname=https://blog.kakaocdn.net/dn/Nc7Xc/btqUejLPGyj/2EExsF5yHNTLjhrGwEqOJk/img.png'
    },
    {
        'story': '원장님으로 테스트를 하면 뭔가 잘될  것도?',
        'img': 'https://newsimg.sedaily.com/2023/11/06/29X4PNBKIV_1.jpg'
    },
]


    return render_template(
                'index.html',
                page_title='잼톡',
                dummy=dummydata,
                alt='로드실패',
                num_images=len(dummydata)
    )
if __name__ == '__main__':
    app.run(debug=True)
