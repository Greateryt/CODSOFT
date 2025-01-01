from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "thecodex9030" 



@app.route('/')
def index():
    varss = session.get('varlist', []) 
    return render_template('index/home.html', varlist=varss)

@app.route('/addcontact')
def addcontact():
    return render_template('index/addcontact.html')

@app.route('/added', methods=['POST'])
def added():
    new_contact = {
        'storeName': request.form.get('storeName'),
        'phone': request.form.get('phone'),
        'email': request.form.get('email'),
        'address': request.form.get('address')
    }

    varlist = session.get('varlist', [])
    varlist.append(new_contact)

    session['varlist'] = varlist

    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_contact(index):
    varlist = session.get('varlist', [])
    if 0 <= index < len(varlist):
        varlist.pop(index) 
        session['varlist'] = varlist
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update_contact(index):
    varlist = session.get('varlist', [])
    if request.method == 'POST':
        varlist[index] = {
            'storeName': request.form.get('storeName'),
            'phone': request.form.get('phone'),
            'email': request.form.get('email'),
            'address': request.form.get('address')
        }
        session['varlist'] = varlist
        return redirect(url_for('index'))
    contact = varlist[index] if 0 <= index < len(varlist) else None
    return render_template('index/updatecontact.html', contact=contact, index=index)

@app.route('/clear')
def clear_session():
    session.pop('varlist', None) 
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
