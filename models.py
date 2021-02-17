from app import db
import enum

class colors(enum.Enum):
	yellow = "YELLOW"
	purple = "PURPLE"
	green = "GREEN"

class Hat(db.Model):
    __tablename__ = 'hat'

    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.Enum(colors))

    def __init__(self, color):
        self.color = color