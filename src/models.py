from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

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
    character_name = db.Column(db.String(250), unique=True, nullable=False)
    character_height = db.Column(db.String(250))
    character_hair_color = db.Column(db.String(250), nullable=False)
    character_skin_color = db.Column(db.String(250), nullable=False)
    character_eyes_color = db.Column(db.String(250), nullable=False)
    character_gender = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.character_name

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "character_height": self.character_height,
            "character_hair_color": self.character_hair_color,
            "character_skin_color": self.character_skin_color,
            "character_eyes_color": self.character_eyes_color,
            "character_gender": self.character_gender,

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
    planet_name = db.Column(db.String(250), nullable=False, unique=True)

    def __repr__(self):
        return '<Planets %r>' % self.planet.name

    def serialize(self):
        return {
            "id": self.id,
            "planet_population": self.planet_population,
            "planet_diameter": self.planet_diameter,
            "planet_climate": self.planet_climate,
            "planet_gravity": self.planet_gravity,
            "planet_name" : self.planet_name,
            
    }

class FavoritesCharacters(db.Model):
    __tablename__ = 'favoritescharacters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    character_id = db.Column (db.Integer, db.ForeignKey('characters.id'))

    def __repr__(self):
        return '<Favoritescharacters %r>' % self.id

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
    user_id = db.Column (db.Integer, db.ForeignKey('User.id'))
    planet_id = db.Column (db.Integer, db.ForeignKey('planets.id'))

    def __repr__(self):
        return '<FavoritesPlanets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
            
    }    

   