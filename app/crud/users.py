from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import UserCreate, UserUpdate
from app.crud.crud_base import CrudBase


class CrudUser(CrudBase[User, UserCreate, UserUpdate]):

    def get_user_by_email(self, db: Session, email: str):
        return self.query(db).filter(User.email == email).first()

    def crud_create_user(self, db: Session, user: UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = User(email=user.email, hashed_password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


crud_users = CrudUser(User)