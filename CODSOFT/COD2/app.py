from flask import Flask, render_template, request, redirect, flash
import random
import string

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index/home.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        length = int(request.form.get('length'))
    except ValueError:
        return render_template('index/home.html', passs=None)

    if 6 <= length <= 20:
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        specialchar = '@#_'

        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(specialchar)
        ]

        allchar = lower + upper + digits + specialchar
        password += random.choices(allchar, k=length - len(password))
        
        random.shuffle(password)
        passs = ''.join(password)

        return render_template('index/home.html', passs=passs)
    else:
        return render_template('index/home.html', passs=None)

if __name__ == "__main__":
    app.run(debug=True)
