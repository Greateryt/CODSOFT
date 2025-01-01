from flask import Flask, render_template, request, session, redirect, url_for
import urllib.parse

app = Flask(__name__)
app.secret_key = "thecodex9030"

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        chrac = request.form.get("char")
        if chrac:
            chrac = urllib.parse.unquote(chrac)
            if chrac != 'C':
                strin = session.get('result', "")
                strin += chrac
                session['result'] = strin
            else:
                session['result'] = "" 
    
    result = session.get('result', "")
    return render_template('index/home.html', resulttt=result)

@app.route('/calculate', methods=["POST"])
def calculate():
    strin = session.get('result', "")
    try:
        calculated = eval(strin)
        session['result'] = str(calculated) 
    except Exception as e:
        session['result'] = "Error" 
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
