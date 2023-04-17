

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):



    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    flavor = db.Column(db.Text, 
                       nullable=False)
    size = db.Column(db.Text, 
                     nullable=False)
    rating = db.Column(db.Float, 
                       nullable=False)
    image = db.Column(db.Text, 
                      nullable=False, 
                      default = 'https://images.unsplash.com/photo-1572451479139-6a308211d8be?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80')
    
    
    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }