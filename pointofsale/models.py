from pointofsale import db


class Menus(db.Model):
    # schema for the Menu model
    id = db.Column(db.Integer, primary_key=True)
    menus_name = db.Column(db.String(25), unique=True, nullable=False)
    menus_description = db.Column(db.String(29), nullable=False)
    submenus = db.relationship("Submenus", backref="menus", cascade="all, delete", lazy=True)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.menus_name, self.menus_description


class Submenus(db.Model):
    # schema for the Submenu model
    id = db.Column(db.Integer, primary_key=True)
    submenu_name = db.Column(db.String(25), unique=True, nullable=False)
    submenu_description = db.Column(db.String(29), nullable=False)
    items = db.relationship("Items", backref="submenu", cascade="all, delete", lazy=True)
    menus_id = db.Column(db.Integer, db.ForeignKey("menus.id"), nullable=False)
    
   

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.submenus_name
    

class Items(db.Model):
    # schema for the Items model
    id = db.Column(db.Integer, primary_key=True)
    items_name = db.Column(db.String(25), unique=True, nullable=False)
    items_description = db.Column(db.String(29), nullable=False)
    items_price = db.Column(db.Float, nullable=False)
    submenus_id = db.Column(db.Integer, db.ForeignKey("submenus.id"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.items_name