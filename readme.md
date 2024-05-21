# Flask life cycle

a simple flask app to show the life cycle of a flask app

## Installation

```bash
pip install flask blinker uwsgi
```

## Usage

```bash
uwsgi --ini uwsgi.ini
```

And open the browser at `http://localhost:9090`, you will see the following output in the console, that shows the life cycle of the flask app

With the "signal received" suffix, you can see the order of the signals that are sent by the flask app

With the "called" suffix, you can see the order of the functions that are called by the flask app

```bash
appcontext_pushed signal received
request_started signal received
URL value preprocessor called
Before request called
Handler function called
After request called
request_finished signal received
Teardown request called
request_tearing_down signal received
Teardown appcontext called
appcontext_tearing_down signal received
appcontext_popped signal received
```
