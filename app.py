import flask
from flask import *
app=Flask(__name__)
#flask.request为请求方式
@app.route('/',methods=['GET',"POST"]) #mthods定义了请求的方式
def imdex():
    if request.method=='POST': #判断请求
        return 'Post qingqiu !'
    else:
        return 'Get qinqiu !'

if __name__ == '__main__':
    app.run()
