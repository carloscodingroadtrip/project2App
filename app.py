from flask import Flask, render_template, jsonify, request, url_for, redirect
from werkzeug.http import HTTP_STATUS_CODES

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.static_folder = 'static'

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return render_template("index.html")


@app.route('/apis')
def apis():
    return(
        f'AVAILABLE API ROUTES: <br>'
        f'_______________________________  <br>'
        f'<br>ALL BABY NAMES....: <br><a href="">/api/babynames</a><br>'
        f'<br>'

        f'BUDGET FILTER ONLY JSON:  /api/budget'
    )

##########  ERROR 404 page not found ##################
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


##########  ERROR HANDLING ##################
def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


############# FLASK CLOSING CODE ###################
if __name__ == '__main__':
    app.run(debug=True)
