# import necessary modules

from flask import render_template, request, redirect, url_for
from pointofsale import app, db
from pointofsale.models import Menus, Submenus, Items, Currentorder, Transactions
import csv, os, datetime

# import necessary modules for email

import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase


@app.route("/")

# initial page that loads at startup

def home():
    return render_template("startscreen.html")


@app.route("/main_menu")
def main_menu():

    # returns a list of all menus

    menus=list(Menus.query.order_by(Menus.menus_name).all())
    return render_template("main_menu.html", menus=menus)


@app.route("/add_menus/<new_menu>", methods=["GET", "POST"])
def add_menus(new_menu):
    if request.method == "POST":
        menus=Menus(
            menus_name=request.form.get("menus_name"),
            menus_description = request.form.get("menus_description")
        )
        db.session.add(menus)
        db.session.commit()
        return redirect(url_for("add_menus", new_menu=True))
    return render_template("add_menus.html", new_menu=new_menu)


@app.route("/edit_menus/<int:menus_id>", methods=["GET", "POST"])
def edit_menus(menus_id):
    menus=Menus.query.get_or_404(menus_id)
    if request.method == "POST":
        menus.menus_name=request.form.get("menus_name"),
        menus.menus_description=request.form.get("menus_description")
        db.session.add(menus)
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("edit_menus.html", menus=menus)


@app.route("/delete_menus/<int:menus_id>", methods=["GET", "POST"])
def delete_menus(menus_id):
    menus=Menus.query.get_or_404(menus_id)
    if request.method == "POST":
        db.session.delete(menus)
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("delete_menus.html", menus=menus)


@app.route("/add_submenus/<int:submenus_id>/<new_submenu>", methods=["GET", "POST"])
def add_submenus(submenus_id, new_submenu):
    submenus=list(Submenus.query.filter_by(menus_id=submenus_id).all())
    menus=Menus.query.get_or_404(submenus_id)
    if request.method == "POST":
        submenus=Submenus(
            submenus_name=request.form.get("submenus_name"),
            submenus_description=request.form.get("submenus_description"),
            menus_id=submenus_id
        )
        db.session.add(submenus)
        db.session.commit()
        return redirect(url_for("add_submenus", submenus_id=submenus_id, new_submenu=True))
    return render_template("add_submenus.html", menus=menus, submenus=submenus, submenus_id=submenus_id, new_submenu=new_submenu)


@app.route("/view_submenus/<int:submenus_id>")
def view_submenus(submenus_id):
    submenus=list(Submenus.query.filter_by(menus_id=submenus_id).order_by(Submenus.submenus_name).all())
    menus=Menus.query.get_or_404(submenus_id)
    return render_template("view_submenus.html",menus=menus, submenus=submenus, submenus_id=submenus_id)


@app.route("/edit_submenus/<int:submenus_id>", methods=["GET", "POST"])
def edit_submenus(submenus_id):
    submenus=Submenus.query.get_or_404(submenus_id)
    menus_name=Submenus.query.get_or_404(submenus.menus_id)
    if request.method == "POST":
        submenus.submenus_name=request.form.get("submenus_name"),
        submenus.submenus_description=request.form.get("submenus_description")
        db.session.add(submenus)
        db.session.commit()
        return redirect(url_for("view_submenus", submenus_id=submenus.menus_id))
    return render_template("edit_submenus.html", submenus=submenus, menus_name=menus_name)


@app.route("/delete_submenus/<int:submenus_id>", methods=["GET", "POST"])
def delete_submenus(submenus_id):
    submenus=Submenus.query.get_or_404(submenus_id)
    if request.method == "POST":
        db.session.delete(submenus)
        db.session.commit()
        return redirect(url_for("view_submenus", submenus_id=submenus.menus_id))
    return render_template("delete_submenus.html", submenus=submenus)


@app.route("/view_items/<int:menus_id>", methods=["GET", "POST"])
def view_items( menus_id):
    submenus=Submenus.query.get_or_404(menus_id)
    items=list(Items.query.filter_by(submenus_id=menus_id).order_by(Items.items_name).all())
    return render_template("view_items.html", items=items, submenus=submenus, menus_id=menus_id)

    
@app.route("/add_items/<int:menus_id>/<new_item>", methods=["GET", "POST"])
def add_items(menus_id, new_item):
    # Gets the submenu associated with the items using the Submenus field menus_id.
    submenus = Submenus.query.get_or_404(menus_id)
    if request.method == "POST":
        items=Items(
        items_name = request.form.get("items_name"),
        items_description = request.form.get("items_description"),
        items_price = request.form.get("items_price"),
        items_costprice = request.form.get("items_costprice"),
        submenus_id = menus_id
        )
        db.session.add(items)
        db.session.commit()
        return redirect(url_for("add_items", menus_id=menus_id, submenus=submenus, new_item=True))
    return render_template("add_items.html", menus_id=menus_id, submenus=submenus, new_item=new_item)


@app.route("/edit_items/<int:submenus_id>", methods=["GET", "POST"])
def edit_items(submenus_id):
    items=Items.query.get_or_404(submenus_id)
    submenus_name = Submenus.query.get_or_404(items.submenus_id)
    if request.method == "POST":
        items.items_name=request.form.get("items_name"),
        items.items_description=request.form.get("items_description"),
        items.items_price=request.form.get("items_price"),
        items.items_costprice=request.form.get("items_costprice")
        db.session.add(items)
        db.session.commit()
        return redirect(url_for("view_items", menus_id=items.submenus_id, items=items))
    return render_template("edit_items.html", submenus_id=submenus_id, items=items, submenus_name=submenus_name)


@app.route("/delete_items/<int:submenus_id>", methods=["GET", "POST"])
def delete_items(submenus_id):
    items=Items.query.get_or_404(submenus_id)
    if request.method == "POST":
        db.session.delete(items)
        db.session.commit()
        return redirect(url_for("view_items", menus_id=items.submenus_id, items=items))
    return render_template("delete_items.html", submenus_id=submenus_id, items=items)


@app.route("/current_order")
# Returns the current order and it's total price.
def current_order():
    current_order = list(Currentorder.query.order_by(Currentorder.id).all())
    total_price, total_costprice=total(current_order)
    return render_template("current_order.html", current_order=current_order, total_price=total_price, total_costprice=total_costprice)


def total(current_order):
    # Function to return the total price and total cost price of the current order.
    total_price = 0
    total_costprice = 0
    for price in current_order:
        total_price += price.currentorder_price
        total_costprice += price.currentorder_costprice
    total_price = round(total_price, 2)
    total_costprice = round(total_costprice, 2)
    return total_price, total_costprice


@app.route("/addto_order/<int:item_id>/<int:submenus_id>/<item_name>/<item_price>/<item_costprice>", methods=["GET", "POST"])
# Adds the selected item to the current order.
def addto_order(item_id, submenus_id, item_name, item_price, item_costprice):
    submenus=Submenus.query.get_or_404(submenus_id)
    items = list(Items.query.filter_by(submenus_id=submenus_id).all())
    current_order=Currentorder(
        currentorder_name = item_name,
        currentorder_price = item_price,
        currentorder_costprice=item_costprice,
        item_id = item_id
    )
    db.session.add(current_order)
    db.session.commit()
    return render_template("view_items.html", menus_id=item_id, submenus_id=submenus_id, submenus=submenus, items=items)


@app.route("/remove_item/<int:item_id>", methods=["GET", "POST"])
# Removes the selected item from the current order.
def remove_item(item_id):
    delete_item = Currentorder.query.get_or_404(item_id)
    item_name = delete_item.currentorder_name
    if request.method == "POST":
        db.session.delete(delete_item)
        db.session.commit()
        return redirect(url_for("current_order"))
    return render_template("remove_item.html", delete_item=delete_item, item_id=item_id, item_name=item_name)


@app.route("/transaction/<total_price>/<total_costprice>")
# Adds the current order to the transactions table by calling the add_transactions function.
def transaction(total_price, total_costprice):
        add_transactions(total_price, total_costprice)
        return render_template("current_order.html", total_price=0)


def add_transactions(total_price, total_costprice):
    current_order = list(Currentorder.query.order_by(Currentorder.id).all())
    for item in current_order:
        add_transaction = Transactions(
            transactions_name=item.currentorder_name,
            transactions_price=item.currentorder_price,
            transactions_costprice=item.currentorder_costprice
        )
        db.session.add(add_transaction)
        delete_item=Currentorder.query.get_or_404(item.id)
        db.session.delete(delete_item)
    add_total=Transactions(
        transactions_name="total",
        transactions_price=total_price,
        transactions_costprice=total_costprice
    )
    db.session.add(add_total)
    db.session.commit()
    return
   

@app.route("/sales")
# returns a list of all current transactions
def sales():
    transactions = list(Transactions.query.order_by(Transactions.id).all())
    return render_template("sales.html", transactions=transactions)


@app.route("/email_sales/<send_address>", methods=["GET", "POST"])
# Sends a .csv file of the days sales to a nominated email address. See readme for credits.
def email_sales(send_address):
    
    if request.method == "POST":
        send_address = request.form.get("email_address")
        transactions = list(Transactions.query.order_by(Transactions.id).all())
        with open("sales_data.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Item Name", "Price", "Cost Price"])
            for transaction in transactions:
                writer.writerow([transaction.transactions_name, transaction.transactions_price, transaction.transactions_costprice])
        days_sales = list(Transactions.query.order_by(Transactions.id).all())
        for sale in days_sales:
            delete_item = Transactions.query.get_or_404(sale.id)
            db.session.delete(delete_item)
        db.session.commit()
        # Send email with sales data
        now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        # Create the body of the message plaintext and HTML.
        emailfrom = "gavin.brown@4uxdesign.com"
        filetosend = "sales_data.csv"
        username = "gavin.brown@4uxdesign.com"
        password = os.environ.get("EMAIL")
        msg = MIMEMultipart()
        msg["From"] = emailfrom
        msg["To"] = send_address
        msg["Subject"] = "sales data .csv for " + now
        msg.preamble = ""
        ctype, encoding = mimetypes.guess_type(filetosend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)
        # Create the attachment of the message in text/csv.
        filetosend='sales_data.csv'
        fp = open(filetosend, 'rb')
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=filetosend)
        msg.attach(attachment)
        # Send the message via SMTP server.
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username,password)
        server.sendmail(emailfrom, send_address, msg.as_string())
        server.quit()
        return redirect(url_for("main_menu"))
    return render_template("email_sales.html", send_address=send_address)


@app.route("/startscreen")
def startscreen():
    # The initial page that loads at startup.
    return render_template("startscreen.html")


