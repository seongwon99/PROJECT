from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    Food=db.Column(db.String(100))
    Water=db.Column(db.Float)
    Protein=db.Column(db.Float)
    Fat=db.Column(db.Float)
    Carbohydrate=db.Column(db.Float)
    Result=db.Column(db.String(100))



# flask db init
# flask db migrate  <===안됨