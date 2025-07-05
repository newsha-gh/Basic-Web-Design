from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template("index.html")
@app.route('/login', methods=['GET'])
def login():
   username = request.args.get('username')
   password = request.args.get('password')
   print(username, password)
   if username == 'newsha' and password == '123456':
      return render_template("success.html")
   else:
      return render_template("failure.html")
app.run()