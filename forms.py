from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired

class ListForm(Form):
    """docstring for ListForm"""
    listTitle = StringField('listTitle')
