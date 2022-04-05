from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import UserCreate, UserUpdate
from app.crud.crud_base import CrudBase
from app.core.security import get_password_hash, verify_password


class CrudUser(CrudBase[User, UserCreate, UserUpdate]):

    def get_user_by_email(self, db: Session, email: str):
        return self.query(db).filter(User.email == email).first()

    def crud_create_user(self, db: Session, user: UserCreate):
        db_user = User(email=user.email, hashed_password=get_password_hash(user.hashed_password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def authenticate_user(self, username: str, password: str, db: Session):
        user = self.get_user_by_email(db, email=username)
        if not user:
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user


crud_users = CrudUser(User)