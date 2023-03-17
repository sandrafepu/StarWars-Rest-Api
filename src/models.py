from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), unique=True, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=False)


    def serialize_all(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

    def serialize_each(self):
        return {
            "id": self.id,
            "properties": {
                "name": self.name,
                "gender": self.gender
            }
        }    

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), unique=True, nullable=False)
    population = db.Column(db.String(20), unique=False, nullable=False)


    def serialize_all(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

    def serialize_each(self):
        return {
            "id": self.id,
            "properties": {
                "name": self.name,
                "population": self.population
            }
        } 