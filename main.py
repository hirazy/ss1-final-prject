from flask import render_template, Flask

app = Flask(__name__, template_folder='templates')

@app.route('/api/list')
def allList():
    con = sql.connect("todoList.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from todo")

    rows = cur.fetchall()

    list = rows
    return jsonify(json.dumps(list))

@app.route('/api/add', methods = ['POST'])
def add():
    description = request.form.get("itemDescription")

    with sql.connect("todoList.db") as con:
        cur = con.cursor()
        cur.execute("INSERT into todo (description, status) values (?,?)", (description, 'Doing'))
        con.commit()

    return redirect('/')

@app.route('/api/update?id=<id>', methods = ['POST'])
def update(id):
    description = request.form.get("")

    status = request.form.get("")


    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

