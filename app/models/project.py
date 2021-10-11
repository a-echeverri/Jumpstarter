from sqlalchemy.orm import relationship
from .db import db


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False, unique=True)
    goal = db.Column(db.Integer, nullable=False)
    current_amount = db.Column(db.Integer, nullable=False)
    categories_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    image_url = db.Column(db.Integer, nullable=False)

    categories = relationship("Category", back_populates="project")
    users = relationship("User", back_populates="project")
