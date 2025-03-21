from flask import Flask, render_template
import random
# 设定对象app
app = Flask(__name__, template_folder='template', static_folder='static')

Method = ['John', 'Smith', 'Judy', 'Louis']

# 定义路径index的返回值, render_template的意思是，在template_folder里面找到一个叫做我们输入的html
@app.get('/index')
def index():
    method = 'By '+ random.choice(Method)
    return render_template('index.html', **{'method':method})

# 现在，我们用数据模拟一下，服务器从数据库里获取数据并且修改展示的网页的过程

# 假设我们得到的数据是：

data = ["Machine Guns", "RPGs", "Bullets", "Armors"]


@app.get('/requirement')
def requirement():
    return render_template('Requirement.html', **{'data': data})

@app.get('/about')
def about():
    return render_template('Test.html')

# 注意：路径名和函数名要对齐。

# 我们通过在HTML网站的head部分加入CSS代码做网页展示的渲染和排版，详情参见Requirement.html

# 而JS一般参与动态变化，比如单击某处出现不同颜色等等

'''
为了方便我们统筹规划大型的html文件，一般将html，CSS，JS文件分开隔离存储管理，所以我们在根目录上放了static
文件夹，来存放这些文件

具体的创建操作是使用StyleSheet文件来创建CSS后缀文件，用JavaScript文件存放script标签下的文件

'''
app.run()
