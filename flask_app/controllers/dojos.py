from flask_app.models.dojo import Dojo
from flask import redirect, render_template, request

from pprint import pprint

from flask_app import app


@app.route("/")
def index():
    return redirect("/dojos")


@app.route("/dojos")
def all_dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos=dojos)


@app.route("/dojos/create", methods=["POST"])
def create_dojo():
    print(request.form)
    Dojo.create(request.form)
    return redirect("/dojos")


@app.route("/dojos/<int:dojo_id>")
def show(dojo_id):
    dojo = Dojo.get_one(dojo_id)
    return render_template("show_dojo.html", dojo=dojo)


# @app.route("/user/edit/<int:id>")
# def edit(id):
#     data = {"id": id}
#     return render_template("edit_user.html", user=User.get_one(data))


# @app.route("/user/new")
# def new():
#     return render_template("new_user.html")


# @app.route("/user/create", methods=["POST"])
# def create():
#     print(request.form)
#     User.save(request.form)
#     return redirect("/users")


# @app.route("/user/edit/<int:id>")
# def edit(id):
#     data = {"id": id}
#     return render_template("edit_user.html", user=User.get_one(data))


# @app.route("/user/show/<int:id>")
# def show(id):
#     data = {"id": id}
#     return render_template("show_user.html", user=User.get_one(data))
