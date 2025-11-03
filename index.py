from flask import Blueprint, render_template

bp_index = Blueprint('index', __name__) 

@bp_index.route('/')
def index():
    return render_template('index.html')

@bp_index.route('/catalog')
def catalog():
    return render_template('catalog.html')