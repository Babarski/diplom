
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from models import Users, Score, Position
import json
import Map

@app.route('/')
@app.route('/index')
def index():
    if 'login' in session:
        return render_template("main_page.html")
    return render_template("login.html")

@app.route('/login', methods = ['POST'])
def login():
    error = None
    users = Users.query.all()
    login_user = None
    rights = 0
    # request.form['nickname'] in users['nickname']
    for user in users:
        if request.form['login'] == user.login:
            login_user = user
            rights = user.isAdmin

    if login_user is not None:
        if request.form['password'] == login_user['password']:
            session['login'] = request.form['login']
            session['rights'] = rights
            return redirect(url_for('main_page'))
        else:
            error = 'Invalid password combination'
            return render_template("login.html", error=error)
    else:
        error = 'Invalid login combination'
        return render_template("login.html", error=error)

@app.route('/add_user', methods = ['GET', 'POST'])
def register():
    error = None
    positions = Position.query.all()
    pos = []
    msg = ""
    for position in positions:
        pos.append(position)

    if request.method == 'POST':

        users = Users.query.all()
        existing_user = False
        for user in users:
            if request.form['login'] == user.login:
                existing_user = True

        if existing_user == False:
            u = Users(login=request.form['login'], email=request.form['email'], password=request.form['password'],
                     name=request.form['name'], surname=request.form['surname'], idposition=request.form['position'],
                      isadmin=request.form['admin'])
            db.session.add(u)
            db.session.commit()
            return redirect(url_for('successful_addition'))


        error = "That login already exists!"
        return render_template('add_user.html', positions = pos,
                               error = error)

    return render_template('add_user.html', error = error, positions = pos)

@app.route('/successful_addition', methods = ["GET"])
def successful_addition():
    if 'login' in session:
        if session['rights'] == 1:
            return render_template('successful_addition.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/add_score', methods = ["GET", "POST"])
def add_score():
    if 'login' in session:
        if request.method == "POST":

            u = Users.query.filter_by(login=session['login']).first()
            s = Score.query.filter_by(idScore = u.idScore).first()
            print s.co
            s.co = request.form['co']
            s.tw = request.form['tw']
            s.ri = request.form['ri']
            s.imp = request.form['imp']
            s.pl = request.form['pl']
            s.me = request.form['me']
            s.cf = request.form['cf']
            s.sh = request.form['sh']
            s.sp = request.form['sp']
            db.session.add(s)
            db.session.commit()
        return render_template('add_score.html')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('index'))


@app.route('/main_page')
def main_page():
    if 'login' in session:
        if session['rights'] == 1:
            return render_template('main_page.html')
        else:
            return render_template('add_score.html')
    else:
        return render_template('login.html')


@app.route('/create_team', methods = ['GET', 'POST'])
def create_team():
    error = None
    users = Users.query.all()
    us = []
    for user in users:
        if user.alreadyInTeam is None or  user.alreadyInTeam == 0:
            us.append(user)

    return render_template('create_team.html',
                           users = us,
                           error = error)

@app.route('/diagnose_team')
def diagnose_team():
    users = Users.query.all()
    for user in users:
        user.team_id = 0
        db.session.commit()
    return render_template('main_page.html')

@app.route('/pass_test')
def pass_test():
    return render_template('pass_test.html')

@app.route('/add_position', methods = ['GET', 'POST'])
def add_position():
    if request.method == "POST":
        position = Position(rank=request.form['rank'], title=request.form['title'])
        db.session.add(position)
        db.session.commit()
    return render_template('add_position.html')

@app.route('/check_team',  methods = ['GET', 'POST'])
def check_team():
    if 'login' in session and session['rights'] == 1:
            if request.method == 'POST':
                teamMemberer = []
                toTeam = []
                for i in range(0, 9):
                    teamMemberer.append(int(request.form['memberId' + str(i)]))

                if any(teamMemberer.count(tn) > 1 for tn in teamMemberer) == False:
                    for member in teamMemberer:
                        u = Users.query.filter_by(idUser = member).first()
                        s = Score.query.filter_by(idScore = u.idScore).first()
                        toTeam.append({
                            'id': u.idUser,
                            'CO':s.co,
                            'TW': s.tw,
                            'RI': s.ri,
                            'IMP': s.imp,
                            'PL': s.pl,
                            'ME': s.me,
                            'CF': s.cf,
                            'SH': s.sh,
                            'SP': s.sp,
                            'func_role': u.idPosition
                        })
                    json_data = json.dumps(toTeam)

                    teamScore, Team, BadRolesCombinations, showBadRoleCombinationsInTwoEmployess = Map.calculations(json_data)
                    roles=["Coordinator", "Team Worker", "Resourse Investigator", "Implementer", "Plant", "Monitor/Evaluator", "Contoller/Finisher", "Shaper", "Specialist"]
                    showEmploeesWithBadRolesCombinations = []
                    showBadRoleCombinationsInTwoEmployess = []

                    for member in BadRolesCombinations:
                        u = Users.query.filter_by(idUser=member[1]).first()
                        showEmploeesWithBadRolesCombinations.append([u.name +" "+ u.surname, roles[member[0]]])
                    for member in BadRolesCombinations:
                        u1 = Users.query.filter_by(idUser=member[0]).first()
                        u2 = Users.query.filter_by(idUser=member[1]).first()
                        showEmploeesWithBadRolesCombinations.append([u1.name +" "+ u1.surname, u2.name +" "+ u2.surname])
                    if Team != []:
                        resultedTeam = []
                        for member in Team:
                            u = Users.query.filter_by(idUser=member[1]+1).first()
                            resultedTeam.append([u.name +" "+ u.surname, roles[member[0]]])

                        return render_template('checking_result.html',
                                               result = "Good",
                                               teamScore=teamScore,
                                               Team=resultedTeam,
                                               showEmploeesWithBadRolesCombinations = showEmploeesWithBadRolesCombinations,
                                               showBadRoleCombinationsInTwoEmployess = showBadRoleCombinationsInTwoEmployess)
                    else:
                        return render_template('checking_result.html',
                                               result = "Not enough points in scores",
                                               showEmploeesWithBadRolesCombinations=showEmploeesWithBadRolesCombinations,
                                               showBadRoleCombinationsInTwoEmployess=showBadRoleCombinationsInTwoEmployess)
                else:
                    error = "Dublicates"
                    users = Users.query.all()
                    us = []
                    for user in users:
                        if user.team_id is None or user.team_id == 0:
                            us.append(user)
                    return render_template('create_team.html',
                                           users=us,
                                           error=error)
    else:
        return render_template('login.html')


    #return render_template('main_page.html')
































