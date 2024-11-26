from flask import Flask, request
app = Flask(__name__)

# サーバールートへアクセスがあった時 --- (*1)


# /hello へアクセスがあった時 --- (*3)
@app.route('/hello')
def hello():
    # nameのパラメータを得る --- (*4)
    name = request.args.get('name')
    word = request.args.get('word')
    
    if name is None:
        name = '名無し'
    if word is None:
        word = 'ひとこと無し'
    # 自己紹介を自動作成
    return """
    <h1>{0}さん、こんにちは！</h1>
    ひとこと：{1}
    """.format(name, word)
if __name__ == '__main__':
    app.run(host='0.0.0.0')

