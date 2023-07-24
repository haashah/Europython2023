from .model import Crime
from sqlalchemy.orm import Session

def get_crime(db: Session, crime_id: int):
    return db.query(Crime).filter(Crime.id == crime_id).first()


def get_crimes(db: Session, crime_id: int):
    return db.query(Crime).all()


def create_crime(db: Session, crime: Crime):
    db.add(crime)
    db.commit()
    db.refresh(crime)
    return crime


def delete_crime(db: Session, crime: Crime):
    crime = db.query(Crime).filter(Crime.id == crime_id).first()
    db.remove(crime)
    db.commit()


def update_crime(db: Session, crime_id: int):
    return db.




