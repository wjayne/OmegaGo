from flask import Blueprint, render_template, request

go = Blueprint('go', __name__)

@go.route('/go')
def go_index():

    return render_template('go/board.html')

# @go.route('/saved')
# def save_board():
#     return render_template('go/board.html')

import json

@go.route('/_array2python')
def array2python():
    wordlist = json.loads(request.args.get('wordlist'))
    # do some stuff
    return jsonify(result=wordlist)