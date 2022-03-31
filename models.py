# coding: utf-8
from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(INTEGER(11), primary_key=True)
    firstname = Column(String(50, 'utf8mb4_unicode_ci'), nullable=False)
    lastname = Column(String(50, 'utf8mb4_unicode_ci'), nullable=False)
    recentvisit = Column(DateTime)


class Item(Base):
    __tablename__ = 'items'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(30, 'utf8mb4_unicode_ci'))
    description = Column(String(1000, 'utf8mb4_unicode_ci'))
    owner_id = Column(INTEGER(11))


class Post(Base):
    __tablename__ = 'posts'

    USER_ID = Column(String(10, 'utf8mb4_unicode_ci'), primary_key=True, nullable=False)
    USER_PASSWD = Column(String(10, 'utf8mb4_unicode_ci'), primary_key=True, nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER(11), primary_key=True)
    email = Column(String(30, 'utf8mb4_unicode_ci'), nullable=False, unique=True)
    hashed_password = Column(String(100, 'utf8mb4_unicode_ci'), nullable=False)
    is_active = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    deleted_at = Column(DateTime)
