from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Students(db.Model):
    __tablename__ = 'students'
    stu_id = db.Column(db.String(20), primary_key=True)
    stu_name = db.Column(db.String(100))
    # ... other fields ...

