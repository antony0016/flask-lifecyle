from flask import Flask, appcontext_pushed,  request_started, request_finished, request_tearing_down, appcontext_tearing_down, appcontext_popped

app = Flask(__name__)


def appcontext_pushed_log(sender, **extra):
    print('appcontext_pushed signal received')


def request_started_log(sender, **extra):
    print('request_started signal received')


def request_finished_log(sender, response, **extra):
    print('request_finished signal received')


def request_tearing_down_log(sender, **extra):
    print('request_tearing_down signal received')


def appcontext_tearing_down_log(sender, **extra):
    print('appcontext_tearing_down signal received')


def appcontext_popped_log(sender, **extra):
    print('appcontext_popped signal received')


# subscribe flask signals
appcontext_pushed.connect(appcontext_pushed_log, app)
request_started.connect(request_started_log, app)
request_finished.connect(request_finished_log, app)
request_tearing_down.connect(request_tearing_down_log, app)
appcontext_tearing_down.connect(appcontext_tearing_down_log, app)
appcontext_popped.connect(appcontext_popped_log, app)


@app.url_value_preprocessor
def get_url_params(endpoint, values):
    print('URL value preprocessor called')


@app.before_request
def before_request():
    print('Before request called')


@app.after_request
def after_request(response):
    print('After request called')
    return response


@app.teardown_request
def teardown_request(error):
    print('Teardown request called')


@app.teardown_appcontext
def teardown_appcontext(error):
    print('Teardown appcontext called')


@app.route('/')
def hello_world():
    print('Handler function called')
    return 'Hello, World!'
