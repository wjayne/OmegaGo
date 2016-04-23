"""Cloud Foundry test"""
"""
TODO: CHANGE THIS FILE SO IT RUNS BY IMPORTING THE APP OBJECT FORM THE MODULE
"""

from flask import render_template
from app import app
import os

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))

@app.route('/')
def hello():
    return render_template('board.html')
    #return 'Hello World! I am running on port ' + str(port)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
