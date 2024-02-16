from pointofsale import db


class Menus(db.Model):
    # schema for the Menu model
    id = db.Column(db.Integer, primary_key=True)
    menu_name = db.Column(db.String(25), unique=True, nullable=False)
    submenu = db.relationship("Submenu", backref="menu", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.menu_name


class Submenus(db.Model):
    # schema for the Submenu model
    id = db.Column(db.Integer, primary_key=True)
    submenu_name = db.Column(db.String(50), unique=True, nullable=False)
    submenu_description = db.Column(db.Text, nullable=False)
    items = db.relationship("Items", backref="submenu", cascade="all, delete", lazy=True)
   

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.submenu_name
    

class Items(db.Model):
    # schema for the Items model
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), unique=True, nullable=False)
    item_description = db.Column(db.Text, nullable=False)
    item_price = db.Column(db.Float, nullable=False)
    submenu_id = db.Column(db.Integer, db.ForeignKey("submenu.id"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.item_name