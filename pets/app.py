from flask import Flask, request, render_template, url_for, redirect, session
from forms import RegisterForm, UpdateForm

app = Flask(__name__)
app.config['SECRET_KEY']="random12432key"

from crud import Crud
crud= Crud()
crud.create_table()

@app.route("/")
def index():
    return render_template("index.html", data=crud.fetch())

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        session.clear()
        for field in form:
            session[field.name] = field.data
        crud.insert_table(session['pet_name'], session['pet_breed'], session['pet_owner'])
        return redirect(url_for("index"))
    return render_template("form.html", form=form, title="Register")

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    form = UpdateForm()
    if form.validate_on_submit():
        session.clear()
        for field in form:
            session[field.name] = field.data
        crud.update_table(session, id)
        return redirect(url_for("index"))
    return render_template("form.html", form=form, title="Update")

@app.route("/delete/<int:id>")
def delete(id):
    crud.delete_entry(id)
    return redirect(url_for("index"))

@app.route("/error/<error>")
def error(error):
    return render_template("error.html", error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5200)
    # close cursor
    crud.cur