from flask import Flask
from flask import session
from flask import redirect
from flask import url_for
from flask import escape
from flask import request
from flask import render_template
import planisphere


app = Flask(__name__)

@app.route('/')
def index():
    # this is used to 'setup' the session with starting values
    session['room'] = planisphere.START
    session['help'] = False
    return redirect(url_for('game'))


@app.route('/game', methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')

    if request.method == 'GET':
        if room_name:
            room = planisphere.load_room(room_name)
            help = session['help']
            session['help'] = False
            return render_template("show_room.html", room=room, help=help)
        else:
            # why is this here? do you need it?
            return render_template("you_died.html")
    else:
        action = request.form.get('action')
        next_room = None

        if room_name and action:
            room = planisphere.load_room(room_name)
            if action == 'help':
                session['help'] = True
            else:
                next_room = room.go(action)

            if not next_room:
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)

            return redirect(url_for('game'))

app.secret_key = 'A\B-F@W I,T/O7?0%LO>?WND*J&F${%['

if __name__=='__main__':
    # app.run(host='192.168.1.4', port=5000, debug=True)
    app.run()
