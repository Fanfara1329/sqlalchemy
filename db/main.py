from flask import Flask
from data import db_session
from data.__all_models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user1 = User()
    user1.surname = "Kik"
    user1.name = "butovsky"
    user1.age = 5
    user1.position = "sailor"
    user1.speciality = "schoolboy"
    user1.address = "module_2"
    user1.email = "kik_kryt@mars.org"
    user1.hashed_password = "krytoi"
    db_sess = db_session.create_session()
    db_sess.add(user1)
    db_sess.commit()
    user2 = User()
    user2.surname = "Medi"
    user2.name = "Блабла"
    user2.age = 13
    user2.position = "sailor"
    user2.speciality = "schoolgirl"
    user2.address = "module_3"
    user2.email = "medi_chief@mars.org"
    user2.hashed_password = "qwerty"
    db_sess = db_session.create_session()
    db_sess.add(user2)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
