from flask import render_template, request, redirect, url_for
from pointofsale import app, db
from pointofsale.models import Menus, Submenus, Items


@app.route("/")
def home():
    return render_template("startscreen.html")


@app.route("/main_menu")
def main_menu():
    menus = list(Menus.query.order_by(Menus.menus_name).all())
    return render_template("main_menu.html", menus=menus)


@app.route("/add_menus", methods=["GET", "POST"])
def add_menus():
    if request.method == "POST":
        menus = Menus(
            menus_name=request.form.get("menus_name"),
            menus_description = request.form.get("menus_description")
        )
        db.session.add(menus)
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("add_menus.html")


@app.route("/edit_menus/<int:menus_id>", methods=["GET", "POST"])
def edit_menus(menus_id):
    menus = Menus.query.get_or_404(menus_id)
    if request.method == "POST":
        menus.menus_name=request.form.get("menus_name"),
        menus.menus_description=request.form.get("menus_description")
        db.session.add(menus)
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("edit_menus.html", menus=menus)


@app.route("/delete_menus/<int:menus_id>", methods=["GET", "POST"])
def delete_menus(menus_id):
    menus = Menus.query.get_or_404(menus_id)
    if request.method == "POST":
        db.session.delete(menus)
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("delete_menus.html", menus=menus)


@app.route("/add_submenus/<int:menus_id>", methods=["GET", "POST"])
def add_submenus(menus_id):
    submenus = Submenus.query.get_or_404(menus_id)
    if request.method == "POST":
        submenus = Submenus(
            submenu_name=request.form.get("submenus_name"),
            submenu_description=request.form.get("submenus_description"),
            menus_id=request.form.get("menus_id")
        )
        db.session.add(submenus)
        db.session.commit()
    return render_template("add_submenus.html", menus_id=menus_id, submenus=submenus)


@app.route("/view_submenus/<int:menus_id>")
def view_submenus(menus_id):
    submenus = list(Submenus.query.filter_by(menus_id=menus_id).all())
    menus = Menus.query.get_or_404(menus_id)
    return render_template("view_submenus.html", menus=menus, submenus=submenus, menus_id=menus_id)


@app.route("/edit_submenus/<int:submenus_id>", methods=["GET", "POST"])
def edit_submenus(submenus_id):
    submenus = Submenus.query.get_or_404(submenus_id)
    if request.method == "POST":
        submenus.submenu_name=request.form.get("submenus_name"),
        submenus.submenu_description=request.form.get("submenus_description")
        db.session.add(submenus)
        db.session.commit()
        return redirect(url_for("view_submenus", menus_id=submenus.menus_id))
    return render_template("edit_submenus.html", submenus=submenus)


@app.route("/delete_submenus/<int:submenus_id>", methods=["GET", "POST"])
def delete_submenus(submenus_id):
    submenus=Submenus.query.get_or_404(submenus_id)
    if request.method == "POST":
        db.session.delete(submenus)
        db.session.commit()
        return redirect(url_for("view_submenus", menus_id=submenus.menus_id))
    return render_template("delete_submenus.html", submenus=submenus)


@app.route("/view_items/<int:menus_id>", methods=["GET", "POST"])
def view_items( menus_id):
    submenus = Submenus.query.get_or_404(menus_id)
    items=list(Items.query.filter_by(submenus_id=menus_id).all())
    return render_template("view_items.html", items=items, menus_id=menus_id, submenus=submenus)


@app.route("/add_items/<int:menus_id>/<int:submenus_id>", methods=["GET", "POST"])
def add_items(submenus_id, menus_id):
    items=list(Items.query.order_by(Items.submenus_id).all())
    submenus=Submenus.query.get_or_404(submenus_id)
    if request.method == "POST":
        items=Items(
            items_name=request.form.get("items_name"),
            items_description=request.form.get("items_description"),
            items_price=request.form.get("items_price"),
            submenus_id=submenus_id
        )
        db.session.add(items)
        db.session.commit()
    return render_template("add_items.html", items=items , submenus_id=submenus_id, menus_id=menus_id, submenus=submenus)


@app.route("/order")
def order():
    return render_template("order.html")


@app.route("/sales")
def sales():
    return render_template("sales.html")


@app.route("/startscreen")
def startscreen():
    return render_template("startscreen.html")
