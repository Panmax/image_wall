# -*- coding: utf-8 -*-

import random

from flask import Flask,render_template
from qiniu import Auth
from qiniu import BucketManager

q = Auth('4Id8GH0H_xu_csRQc0cxxS5Xb2EsIWIA1WtF_WaN', 'YBXzSnmRbrCBufLFoJGZgoAiUR53-liC_btg6_5N')

app = Flask(__name__)


def list_all(bucket_name, bucket=None, prefix=None, limit=None):
    photos = []
    if bucket is None:
        bucket = BucketManager(q)
    marker = None
    eof = False
    while eof is False:
        ret, eof, info = bucket.list(bucket_name, prefix=prefix, marker=marker, limit=limit)
        marker = ret.get('marker', None)
        for item in ret['items']:
            print(item['key'])
            photos.append(item['key'])
    if eof is not True:
        # 错误处理
        pass
    return photos


@app.route('/')
def hello_world():
    photos = list_all('gaodanjiao', prefix='photo', limit=100)
    random.shuffle(photos)
    return render_template('index.html', photos=photos)


if __name__ == '__main__':
    app.run()
