from pprint import pprint
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask import redirect, render_template, request


@app.route("/ninjas")
def new_ninja():
    """Displays the ninjas form."""
    dojos = Dojo.get_all()
    return render_template("ninjas.html", dojos=dojos)


@app.post("/ninjas/create")
def create_ninja():
    Ninja.create(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")
