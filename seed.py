from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    
)

c3 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    
)

c4 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=10
    
)

c5 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=7,
    
)

c6 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=8
    
)

db.session.add_all([c1, c2, c3, c4, c5, c6])

db.session.commit()