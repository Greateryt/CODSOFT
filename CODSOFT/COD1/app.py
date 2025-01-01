from flask import Flask , request , render_template ,redirect ,url_for

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index/todo.html',messages=messages)

@app.route('/submit',methods=['POST','GET'])
def submit():
    element = request.form.get('element')
    if element:
        messages.append({'id':len(messages)+1,'element':element})
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>',methods=['get'])
def delete(item_id):
    global messages
    messages = [item for item in messages if item['id']!= item_id]
    return redirect(url_for('index'))

@app.route('/update/<int:item_id>')
def update(item_id):
    return render_template('index/update.html',item_id=item_id,messages=messages)

@app.route('/updated',methods=['POST','get'])
def updated():
    id= int(request.form.get('item_id'))
    elem = request.form.get('element')
    for item in messages:
        if item['id']==id:
            item['element']=elem
            break
    print(elem)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)