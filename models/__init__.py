from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey, String, Text, DateTime
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:1998@localhost/student_management",echo = True)
Base = declarative_base()
session = Session(engine)

class Users(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50))
  password = Column(String(50))
  details = relationship("UserDetails")

class UserDetails(Base):
  __tablename__ = 'user_details'
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  user_role = Column(String(50))
  subject_teacher = Column(String(50))
  class_teacher = Column(String(50), unique=True)
  student_mark = Column(Integer)
  student_class = Column(String(50))