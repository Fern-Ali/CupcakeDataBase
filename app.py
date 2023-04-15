
from flask import Flask, request, jsonify, render_template, json
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "we-so-secret"


debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def get_home_page():
    cupcakes = Cupcake.query.all()
    return render_template('home.html', cupcakes=cupcakes)

@app.route('/api/cupcakes') 
def list_cupcakes():
    cupcakes = Cupcake.query.all()
    all_cupcakes = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes = all_cupcakes)
   

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    
    if request.json["image"]:
        new_cupcake = Cupcake(flavor=request.json["flavor"],
                              size=request.json["size"],
                              rating=request.json["rating"],
                              image=request.json["image"])
        db.session.add(new_cupcake)
        db.session.commit()
        print(request.json)
    
        return (jsonify(cupcake=new_cupcake.serialize()), 201)
    else:
        new_cupcake = Cupcake(flavor=request.json["flavor"],
                              size=request.json["size"],
                              rating=request.json["rating"]
                              )
        db.session.add(new_cupcake)
        db.session.commit()
        print(request.json)


@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    
    #db.session.query(Cupcake).filter_by(id=id).update(request.json) solution in one line to update from user. dont have to update things line by line.
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)

    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

    #you can type one things or all things, and itll update, filling missing values w/ whats already there.


@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")
    