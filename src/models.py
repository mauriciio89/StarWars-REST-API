from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,

    # do not serialize the password, its a security breach
    }

    

class Characters(db.Model):
    __tablename__ ='characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(250))
    character_height = db.Column(db.String(250))
    character_hair_color = db.Column(db.String(250), nullable=False)
    character_skin_color = db.Column(db.String(250), nullable=False)
    character_eyes_color = db.Column(db.String(250), nullable=False)
    character_gender = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.character_height,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eyes_color": self.eyes_color,
            "gender": self.gender

    # do not serialize the password, its a security breach
    }

   

class Planets(db.Model):
    __tablename__ ='planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    planet_population = db.Column(db.Integer, primary_key=True)
    planet_diameter = db.Column(db.Integer, primary_key=True)
    planet_climate = db.Column(db.String(250), nullable=False)
    planet_gravity = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "planet_population": self.name,
            "planet_diameter": self.character_height,
            "planet_climate": self.hair_color,
            "planet_gravity": self.skin_color
            
    }

class FavoritesCharacters(db.Model):
    __tablename__ = 'favoritescharacters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column (db.Integer, db.ForeignKey('characters.id'))

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
            
    }

    

class FavoritesPlanets(db.Model):
    __tablename__ = 'favoritesplanets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column (db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column (db.Integer, db.ForeignKey('planets.id'))

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
            
    }    

   