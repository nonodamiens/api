from app import db
import enum

class colors(enum.Enum):
	YELLOW = "YELLOW"
	PURPLE = "PURPLE"
	GREEN = "GREEN"

class Hat(db.Model):
    __tablename__ = 'hats'

    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.Enum(colors))

    def __init__(self, color):
        self.color = color