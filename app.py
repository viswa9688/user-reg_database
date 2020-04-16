from flask import Flask,render_template

#standard flask instruction set by python community to call Flask 

app=Flask(__name__)


app.secret_key='replace later'

@app.route("/",methods=['GET','POST'])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
