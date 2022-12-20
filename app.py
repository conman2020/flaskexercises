from flask import Flask, render_template, flash, redirect, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Employee, Department

from forms import AddSnackForm
from forms import UserForm
from forms import NewEmployeeForm
app = Flask(__name__)
app.app_context().push()
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_wtforms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def homepage():
    """Show homepage links."""
    # raise

    return render_template("index.html")

@app.route('/phones')
def list_phones():
    """Renders directory of employees and phone numbers  (from dept)"""
    emps = Employee.query.all()
    return render_template('phones.html', emps=emps)


@app.route("/add", methods=["GET", "POST"])
def add_snack():
    """Snack add form; handle adding."""
    print(request.form)
    form = AddSnackForm()
    # raise

    if form.validate_on_submit():
        print(form.name.data)
        print(form.price.data)
        name = form.name.data
        price = form.price.data
        quantity=form.quantity.data
        flash(f"Added {name} at {price} and quantity of {quantity}")
        return redirect("/")

    else:
        return render_template(
            "snack_add_form.html", form=form)


@app.route("/users/<int:uid>/edit", methods=["GET", "POST"])
def edit_user(uid):
    """Show user edit form and handle edit."""

    user = User.query.get_or_404(uid)
    form = UserForm(obj=user)

    if form.validate_on_submit():
        user.name = form.name.data
        user.email = form.email.data
        db.session.commit()
        flash(f"User {uid} updated!")
        return redirect(f"/users/{uid}/edit")

    else:
        return render_template("user_form.html", form=form)


@app.route('/employees/new', methods=["GET", "POST"])
def show_results():
    form= NewEmployeeForm()
    depts = db.session.query(Department.dept_code, Department.dept_name)
    form.dept_code.choices = depts
    if form.validate_on_submit():
        name= form.name.data
        state= form.state.data
        dept_code= form.dept_code.data
        emp = Employee(name=name, state=state, dept_code=dept_code)
        db.session.add(emp)
        db.session.commit()
        return redirect('/phones')
    else:
        return render_template('add_employee_form.html', form=form)