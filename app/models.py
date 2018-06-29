# coding=utf-8
from app import db

class Position(db.Model):
    __tablename__ = "Position"
    idPosition = db.Column('idPosition', db.Integer, primary_key= True, autoincrement = True)
    rank = db.Column('rank', db.Integer)
    title = db.Column('title', db.String(60))

    def __init__(self, rank, title):
        self.rank = rank
        self.title = title

    def __getitem__(self, item):
        if item == "idPosition":
            return self.idPosition


class Score(db.Model):
    __tablename__ = "Score"
    idScore = db.Column('idScore', db.Integer, primary_key= True, autoincrement = True)
    co = db.Column('co', db.Integer)
    tw = db.Column('tw', db.Integer)
    ri = db.Column('ri', db.Integer)
    imp = db.Column('imp', db.Integer)
    pl = db.Column('pl', db.Integer)
    me = db.Column('me', db.Integer)
    cf = db.Column('cf', db.Integer)
    sh = db.Column('sh', db.Integer)
    sp = db.Column('sp', db.Integer)

    def __getitem__(self, item):
        if item == "idScore":
            return self.idScore

    def __init__(self, co, tw, ri, imp, pl, me, cf, sh, sp):
        self.co = co
        self.tw = tw
        self.ri = ri
        self.imp = imp
        self.pl = pl
        self.me = me
        self.cf = cf
        self.sh = sh
        self.sp = sp


class Users(db.Model):
    __tablename__ = 'Users'
    idUser = db.Column('idUSer', db.Integer, primary_key= True, autoincrement = True)
    login = db.Column('login', db.String(60))
    password = db.Column('password', db.String(60))
    email = db.Column('email', db.String(60))
    name = db.Column('name', db.String(60))
    surname = db.Column('surname', db.String(60))
    idPosition = db.Column('idPosition', db.Integer, db.ForeignKey(Position.idPosition))
    idScore =  db.Column('idScore', db.Integer, db.ForeignKey(Score.idScore))
    alreadyInTeam = db.Column('alreadyInTeam', db.Integer)
    isAdmin = db.Column('isAdmin', db.Integer)

    def __getitem__(self, item):
        if item == 'password':
            return self.password

    def __init__(self, password, login, email, name, surname, idposition, isadmin):
        self.email = email
        self.password = password
        self.login = login
        self.name = name
        self.surname = surname
        self.idPosition = idposition
        self.alreadyInTeam = 0
        self.isAdmin = isadmin
        s = Score(0,0,0,0,0,0,0,0,0)
        db.session.add(s)
        db.session.commit()
        self.idScore = s.idScore

    def __set__(self, instance, value):
        pass
