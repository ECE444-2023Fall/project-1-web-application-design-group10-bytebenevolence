from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = ']%<96hX:3Pv+'
bootstrap = Bootstrap(app)
moment = Moment(app)

from .routes import *
app.register_blueprint(home_page)
app.register_blueprint(login_page)
app.register_blueprint(user_page)
app.register_blueprint(signup_page)
app.register_blueprint(calendar_page)
app.register_blueprint(events_page)
app.register_blueprint(create_event_page)
app.register_blueprint(registration_page)
app.register_blueprint(force_reload_page)


app.register_blueprint(search_page) 
app.register_blueprint(filter_dates)
