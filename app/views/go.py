from flask import Blueprint, render_template

go = Blueprint('go', __name__)

@go.route('/go')
def go_index():
    return render_template('go/go.html')
