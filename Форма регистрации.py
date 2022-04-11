from data.__all_models import User
from flask import Flask, template_rendered, request, render_template
from data import db_session
import forms

app = Flask(__name__)
db_session.global_init("db/flea.db")
app.config['SECRET_KEY'] = 'abobys'


@app.route('/register', methods=['POST', 'GET'])
def registration():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        print(90)

    elif request.method == 'POST':
        user = User(email=form.email.data,
                    password=form.password.data,
                    surname=form.surname.data,
                    age=form.age.data,
                    position=form.position.data,
                    speciality=form.speciality.data,
                    address=form.address.data
                    )
        s = db_session.create_session()
        s.add(user)
        s.commit()
        s.close()
        return "Отправлена"
    return render_template('registration.html', title='Register', form=form)


db_sess = db_session.create_session()
db_sess.commit()

app.run(port=8080, debug=True)
