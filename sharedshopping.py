import os
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from logging import DEBUG

from forms import ListForm
import models

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'g#Xns\xd2\x04d\x15NG\xc7@\xef\x10\x1b\xa3\x1e\xc2\xf6\x8f\xbekt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sharedshopping.db')
db = SQLAlchemy(app)

app.logger.setLevel(DEBUG)

# Page routing

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ListForm()
    if form.validate_on_submit():
        store_list(form)
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

# Error routing

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# Application Logic

def store_list(form):
    # Store list through model
    list = models.List(name=form.listTitle.data, creator_id=1)
    db.session.add(list)
    db.session.commit()
    flash("New List Created -> {}".format(str(list.name)))



if __name__ == '__main__':
    app.run(debug=True)
