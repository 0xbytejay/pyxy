from flask import Flask
from flask import request, render_template
app = Flask(__name__,template_folder="./wwwroot",static_url_path="",static_folder="./wwwroot")


@app.route('/')
def index():
    return render_template("index.html")





@app.route("/login",methods=['GET'])   #请求方式为get
def login():
    return render_template('login.html')


# @app.route("/login",methods=['POST']) #请求方式为post
# def loginin():
#     if request.form['username']=='zkx' and request.form['password']=='zkx':
#             username =request.form['username']
#             return render_template('l.html',username='zkx',moban='moban')
#     return render_template('one.html',username='username',moban='shurucuowu')

@app.route("/register", methods=["GET"])
def register():
    return render_template('register.html')

    
if __name__ == '__main__':
    app.run()