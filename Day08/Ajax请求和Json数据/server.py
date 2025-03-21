from flask import Flask, jsonify, render_template
import json

app = Flask(__name__, template_folder='template', static_folder='static')


@app.get('/')
def index():
    return render_template('test.html')


book = ['A', 'B', 'C', 'D']


@app.get('/ajax')
def ajax():
    return jsonify(book)


json_dic = [{'bookA': 100}, {'bookB': 200}, {'bookC': 300}]


@app.get('/json')
def json():
    return json_dic, jsonify(json_dic), json.dumps(json_dic)

'''
这里返回的后两种数据不一样，因为jsonify会声明一个content-type为json，
但是只做json.dumps就发送会让客户端只收到文本响应导致客户端不会对得到的数据进行解码
'''

app.run()

# 请注意，ajax请求一般会配上json来取数据，然后自己做一些分析来响应到网页
