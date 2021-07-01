from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from flask_session import Session
import psycopg2
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/bank2'
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     login = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
#
#     def __init__(self,  login=None, password=None, account_id=None):
#         self.login = login
#         self.password = password
#         self.account_id = account_id
#     def __repr__(self):
#         #return '%r' % self.account_id
#         return f'User(login={self.login}, id={self.account_id})'
#
#
# class Project(db.Model):
#     __tablename__ = 'projects'
#     id = db.Column(db.Integer, primary_key=True)
#     login = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
#
#     def __init__(self,  login=None, password=None, account_id=None):
#         self.login = login
#         self.password = password
#         self.account_id = account_id
#     def __repr__(self):
#         return f'Project(login={self.login}, accid={self.account_id})'
#
#
# class Account(db.Model):
#     __tablename__ = 'accounts'
#     id = db.Column(db.Integer, primary_key=True)
#     balance = db.Column(db.Integer, nullable=False)
#
#     def __init__(self, balance=None):
#         self.balance = balance
#     def __repr__(self):
#         return f'Account(id={self.id},balance={self.balance})'
#
#
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)
#
# @app.route('/')
# def index():
#     if  session.get("name") == None:
#         return redirect("/login")
#     else:
#         return redirect(url_for('.accc'))
#     # return render_template('index.html')
#
#
# @app.route('/login/', methods=['POST', 'GET'])
# def loginn():
#     error = ""
#     me = Users('admin2', 'admin')
#     db.session.add(me)
#     db.session.commit()
#     if request.method == 'POST':
#         if valid_login_and_password(str(request.form.get('username')), str(request.form.get('password')), str(request.form.get('check'))):
#             get_accid(str(request.form.get('username')), str(request.form.get('check')))
#             session["name"] = request.form.get("username")
#             return redirect(url_for('.accc'))
#         else:
#             error = 'Invalid username/password'
#     return render_template('login.html', error=error)
#
#
# def get_accid(login, check):
#     accid = ''
#     if check == 'on':
#         accid = Project.query.filter_by(login=login).first_or_404()
#     else:
#         accid = User.query.filter_by(login=login).first_or_404()
#     session["id"] = str(accid.id)
#     return 0
#
#
# def valid_login_and_password(login, password,check):
#     if check == 'on':
#         user = Project.query.filter_by(login=login, password=password).first()
#     else:
#         user = User.query.filter_by(login=login, password=password).first()
#     if user!=None:
#         return True
#     else:
#         return False
#
#
# @app.route('/account/', methods=['POST', 'GET'])
# def accc():
#
#     name = session.get("name")
#     print(request.form.get('log_out'))
#     #select = "SELECT balance FROM accounts WHERE account_id="+session.get('id')+""
#     #cur.execute(select)
#     balance = 0
#     account=Account.query.filter_by(id=session.get('id')).first()
#     print(account.balance)
#     balance=account.balance
#     # for row in cur.fetchall():
#     #     balance = int(row[0])
#     if request.method == 'POST' and request.form.get('log_out') == 'log out':
#         session["name"] = None
#         return redirect("/")
#     if request.method == 'POST' and request.form.get('transactions') == 'transactions':
#         return redirect('transactions')
#
#     return render_template('account.html', name=name, balance=balance)
#
#
# @app.route('/register', methods=['POST', 'GET'])
# def registration():
#     error = ""
#     if request.method == 'POST':
#         if valid_login(str(request.form.get('username')),str(request.form.get('password'))):
#             save(str(request.form.get('username')), str(request.form.get('password')), str(request.form.get('check')))
#             session["name"] = request.form.get("username")
#             return redirect(url_for('.accc'))
#         else:
#             error = 'Invalid username/password'
#     return render_template('regist.html', error=error)
#
#
# def save(login, password, check):
#     me = Account(1000)
#     db.session.add(me)
#     db.session.commit()
#     accid = Account.query.filter().all()
#     print(accid)
#     #session["id"] = str(accid.id)
#     # if check == 'on':
#     #     insert = "INSERT INTO projects (project_login, project_password,account_id) VALUES ('" + login + "', '" + password + "', " + str(id) + ");"
#     # else:
#     #     insert = "INSERT INTO users (user_login, user_password,account_id) VALUES ('" + login + "', '" + password + "', "+str(id)+")"                                                                                                                                                  ";"
#
#
#
# def valid_login(login, password):
#     user1 = Project.query.filter_by(login=login, password=password).first()
#     user2 = User.query.filter_by(login=login, password=password).first()
#     if user1 == None and user2 == None:
#         return True
#     else:
#         return False


dbconfig = {'host': 'localhost',
                'user': 'postgres',
                'port': '5432',
                'password': 'postgres',
                'database': 'bank'}
conn = psycopg2.connect(**dbconfig)
conn.autocommit = True
cur = conn.cursor()


@app.route('/')
def index():
    if  session.get("name") == None:
        return redirect("/login")
    else:
        return redirect(url_for('.accc'))
    # return render_template('index.html')


@app.route('/login/', methods=['POST', 'GET'])
def loginn():
    error = ""
    if request.method == 'POST':
        if valid_login_and_password(str(request.form.get('username')), str(request.form.get('password')), str(request.form.get('check'))):
            session["name"] = request.form.get("username")
            get_accid(request.form.get("username"), str(request.form.get('check')))
            return redirect(url_for('.accc'))
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


def get_accid(name, check):

    if check == 'on':
        select = "SELECT account_id FROM projects WHERE project_login='"+name+"'"
    else:
        select = "SELECT account_id FROM users WHERE user_login='"+name+"'"
    cur.execute(select)
    for row in cur.fetchall():
        session["id"] = str(row[0])
    return 0


def valid_login_and_password(login, password, check):
    if check == 'on':
        select = """SELECT project_login,project_password FROM projects"""
    else:
        select = """SELECT user_login,user_password FROM users"""
    cur.execute(select)
    booll = False
    for row in cur.fetchall():
        if login == str(row[0]) and password == str(row[1]):
            booll = True
    return booll

@app.route("/api", methods=['POST', 'GET'])
def api():
    error = ''
    if request.method == 'GET':
        ac_id = okpolzvl(request.args.get('from'), request.args.get('password'))
        if ac_id:
            if valid_user(request.args.get('to')):
                if check_balance_api(request.args.get('amount'), ac_id):
                    spisanie(request.args.get('from'), request.args.get('amount'))
                    nachislenie(request.args.get('to'), request.args.get('amount'))
                    savetran(request.args.get('from'), request.args.get('to'), request.args.get('amount'), request.args.get('comment'))
                    error = 'success'
                else:
                    error = "You don't have enough money"
            else:
                error = "User doesn't exist"
        else:
            error = "password error"
    return jsonify({"answer": error})


def check_balance_api(amount, nn):
    select = "SELECT balance FROM accounts WHERE account_id=" + nn + ""
    cur.execute(select)
    balance = 0
    for row in cur.fetchall():
        balance = int(row[0])
    if int(amount) > balance:
        return False
    else:
        return True

def okpolzvl(login, password):
    select = "SELECT project_login, project_password FROM projects WHERE project_login='"+login+"' and user_password='"+password+"'"
    cur.execute(select)
    booll = True
    for row in cur.fetchall():
        print(str(row[0]))
        if login == str(row[0]):
            booll = False
    select = "SELECT user_login, user_password FROM users WHERE user_login='"+login+"' and user_password='"+password+"'"
    cur.execute(select)
    for row in cur.fetchall():
        print(str(row[0]))
        if login == str(row[0]):
            booll = False
    return booll
@app.route('/register', methods=['POST', 'GET'])
def registration():
    error = ""
    if request.method == 'POST':
        if valid_login(str(request.form.get('username')),str(request.form.get('password'))):
            save(str(request.form.get('username')), str(request.form.get('password')), str(request.form.get('check')))
            session["name"] = request.form.get("username")
            return redirect(url_for('.accc'))
        else:
            error = 'Invalid username/password'
    return render_template('regist.html', error=error)


def save(login, password, check):
    save = "INSERT INTO accounts(balance) VALUES (1000)"
    cur.execute(save)
    conn.commit()
    accid = "SELECT max(account_id) FROM accounts "
    cur.execute(accid)
    id = ''
    for row in cur.fetchall():
        id = row[0]
    session["id"] = str(id)
    if check == 'on':
        insert = "INSERT INTO projects (project_login, project_password,account_id) VALUES ('" + login + "', '" + password + "', " + str(id) + ");"
    else:
        insert = "INSERT INTO users (user_login, user_password,account_id) VALUES ('" + login + "', '" + password + "', "+str(id)+")"                                                                                                                                                  ";"
    cur.execute(insert)
    conn.commit()


def valid_login(login, password):
    select = """SELECT project_login FROM projects"""
    cur.execute(select)
    booll = True
    for row in cur.fetchall():
        print(str(row[0]))
        if login == str(row[0]):
            booll = False
    select = """SELECT user_login FROM users"""
    cur.execute(select)
    for row in cur.fetchall():
        print(str(row[0]))
        if login == str(row[0]):
            booll = False
    if len(login) < 2 or len(password) < 2:
        booll = False
    return booll


@app.route('/account/', methods=['POST', 'GET'])
def accc():
    name = session.get("name")
    balance()
    if request.method == 'POST' and request.form.get('log_out') == 'log out':
        session["name"] = None
        return redirect("/")
    if request.method == 'POST' and request.form.get('transactions') == 'transactions':
        return redirect('transactions')

    return render_template('account.html', name=name)


@app.route('/api/account/balance', methods=['GET'])
def balance():
    select = "SELECT balance FROM accounts WHERE account_id=" + session.get('id') + ""
    cur.execute(select)
    balancee = 0
    for row in cur.fetchall():
        balancee = int(row[0])
    return jsonify({"balance": balancee})
# @app.route('/api/accounts/data/', methods=['GET'])
# def Api_data():
#     print('work')
#     accid = session.get('id')
#     select = "SELECT transaction_time, sum(amount) FROM transactions WHERE account_id_to=" + accid + " GROUP BY transaction_time"
#     cur.execute(select)
#     rows = cur.fetchall()
#     allmoney = []
#     allmoney.append(['Time', 'number'])
#     for row in rows:
#         allmoney.append([str(row[0]), row[1]])
#
#     print(allmoney)
#     return jsonify({"VALS":allmoney})
@app.route('/account/transactions', methods=['POST', 'GET'])
def money():
    error = ''
    if request.method == 'POST':
        if session.get("name") != None:
            if valid_user(request.form.get('to')):
                if check_amount(request.form.get('amount')):
                    if check_balance(request.form.get('amount')):
                        spisanie(session.get('id'), request.form.get('amount'))
                        nachislenie(request.form.get('to'), request.form.get('amount'))
                        savetran(session.get('id'), request.form.get('to'), request.form.get('amount'), request.form.get('comment'))
                        return redirect(url_for('.accc'))
                    else:
                        error = "You don't have enough money"
                else:
                    error = "Invalid amount"
            else:
                error = "User doesn't exist"
        else:
            error = "You don't log in"
    return render_template('transactions.html', error=error)


def check_amount(amount):
    return str(amount).isnumeric()
def is_it_project(name):
    select = """SELECT project_login FROM projects"""
    cur.execute(select)
    print(name)
    booll = False
    for login in cur.fetchall():
        print(str(login[0]))
        if name == str(login[0]):
            booll = True
    return booll


def check_balance(amount):
    select = "SELECT balance FROM accounts WHERE account_id="+session.get('id')+""
    cur.execute(select)
    balance = 0
    for row in cur.fetchall():
        balance = int(row[0])
    if int(amount) > balance:
        return False
    else:
        return True


def valid_user(name):
    select = """SELECT project_login FROM projects"""
    cur.execute(select)
    booll = False
    for row in cur.fetchall():
        if name == str(row[0]):
            booll = True
    select = """SELECT user_login FROM users"""
    cur.execute(select)
    for row in cur.fetchall():
        if name == str(row[0]):
            booll = True
    return booll


def spisanie(id, amount):
    select = "SELECT balance FROM accounts WHERE account_id="+id+""
    cur.execute(select)
    balance = 0
    for row in cur.fetchall():
        balance = int(row[0])
    balance -= int(amount)
    update = "UPDATE accounts SET balance="+str(balance)+"WHERE account_id="+id
    cur.execute(update)
    conn.commit()


def nachislenie(name, amount):
    if is_it_project(name):
        select = "SELECT account_id FROM projects WHERE project_login='"+name+"'"
    else:
        select = "SELECT account_id FROM users WHERE user_login='"+name+"'"
    cur.execute(select)
    id = ''
    for row in cur.fetchall():
        id = str(row[0])
    select = "SELECT balance FROM accounts WHERE account_id=" + id + ""
    cur.execute(select)
    balance = 0
    for row in cur.fetchall():
        balance = int(row[0])
    balance += int(amount)
    update = "UPDATE accounts SET balance=" + str(balance) + "WHERE account_id=" + id
    cur.execute(update)
    conn.commit()


def savetran(idfrom, name, amount, comment):
    if is_it_project(name):
        select = "SELECT account_id FROM projects WHERE project_login='"+name+"'"
    else:
        select = "SELECT account_id FROM users WHERE user_login='"+name+"'"
    cur.execute(select)
    idto = ''
    for row in cur.fetchall():
        idto = str(row[0])
    insert = "INSERT INTO transactions(account_id_from,account_id_to,amount,comment_) VALUES ("+idfrom+", "+idto+", "+amount+", '"+str(comment)+"')"
    cur.execute(insert)
    conn.commit()


if __name__ == "__main__":

    app.run()
    cur.close()
    conn.close()
#db.create_all()
