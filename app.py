#-*-coding:utf-8-*-

from flask import Flask, render_template, request, jsonify
from config import BUCKET_NAME, CALLBACK_URL, Q_DOMAIN, TOKEN_EXPIRE, FILE_EXPIRE, PRIVATE_BUCKET
from q import q

app = Flask(__name__)


@app.route('/')
def index():
    token_valid_time = TOKEN_EXPIRE
    up_token=q.upload_token(BUCKET_NAME, None, token_valid_time, {'callbackUrl':CALLBACK_URL, 'callbackBody':"key=$(x:key)"})

    return render_template('index.html', up_token=up_token)


@app.route('/callback', methods=['POST'])
def upload_callback():
    key = request.form['key']
    file_url = Q_DOMAIN + key
    if (PRIVATE_BUCKET):
        download_url = q.private_download_url(file_url, expires=FILE_EXPIRE)
    else:
        download_url = file_url

    return jsonify(download_url=download_url)


if __name__ == '__main__':
    app.run(debug=True)

