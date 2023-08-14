# server
# import the app from flask_app
from flask_app import app

# DON'T FORGET TO IMPORT YOUR CONTROLLERS
import flask_app.controllers.dojos
import flask_app.controllers.ninjas

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5012)
