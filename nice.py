from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""
    return """<!doctype html><html><a href="/hello"> LINK </a> Hi! This is the home page. </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <input type="submit"><br>

          <input type="radio" name="group1" value="awesome">"awesome"<br>
          <input type="radio" name="group1" value="terrific"> "terrific"<br>
          <input type="radio" name="group1" value="fantastic"> "fantastic"<br>
          <input type="radio" name="group1" value="neato"> "neato"<br>
          <input type="radio" name="group1" value="fantabulous"> "fantabulous"<br>
          <input type="radio" name="group1" value="wowza"> "wowza"<br>



        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
  
    player = request.args.get("person")


    compliment = request.args.get("group1")
    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
