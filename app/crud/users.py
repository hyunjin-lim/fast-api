from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import UserCreate, UserUpdate
from app.crud.crud_base import CrudBase
from app.core.security import get_password_hash


class CrudUser(CrudBase[User, UserCreate, UserUpdate]):

    def get_user_by_email(self, db: Session, email: str):
        return self.query(db).filter(User.email == email).first()

    def crud_create_item(self, db: Session, user: UserCreate):
        db_user = User(email=user.email, hashed_password=get_password_hash(user.password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


crud_users = CrudUser(User)