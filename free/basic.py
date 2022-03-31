from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sites = ['DC1', 'DC2', 'DC3', 'DC4']
    return render_template('index.html', sites=sites)

@app.route('/switchinfo', methods=['GET','POST'])
def switchinfo():

    name = 

    return render_template("mat.html",name=name)

if __name__ == "__main__":
    app.run(debug=True)
