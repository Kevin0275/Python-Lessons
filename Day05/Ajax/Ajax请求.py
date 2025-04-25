# 为了避免一次性获取大量数据导致浏览器崩溃，我们设定这样一个功能：只有当用户点击的时候，才发送请求获取数据。
# 也就是二次请求。
from flask import Flask, render_template

# 我们可以选择将信息全部塞给客户端，然后让客户端用js判断是否应该弹出
# 当然，我们也可以让客户端再发一次请求！

'''
这样当用户进行操作，客户端向服务器发送请求获取数据，再局部刷新的方式叫做Ajax请求，注意，是局部刷新，网页并没有刷新。
'''

app = Flask(__name__, template_folder='template',static_folder='static')

book = ['Sherlock', 'Iron man', 'Spiderman']


@app.get('/')
def index():
    return render_template('index.html', **{'books': book})

@app.get('/books')
def books():
    return book
app.run()
