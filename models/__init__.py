from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey, String, Text, DateTime
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:1998@localhost/student_management",echo = True)
Base = declarative_base()
session = Session(engine)

class College(Base):
  __tablename__ = 'college'
  id = Column(Integer, primary_key=True)
  name = Column(String(50)) 
  location = Column(Text)

class Departments(Base):
  __tablename__ = 'departments'
  id = Column(Integer, primary_key=True)
  name = Column(String(50))

class Subjects(Base):
  __tablename__ = 'subjects'
  id = Column(String(50), primary_key=True)
  name = Column(Text)
  department_id = Column(Integer)

class Users(Base):
  __tablename__ = 'users'
  id = Column(String(50), primary_key=True)
  encrypted_data = Column(Text)

class Professors(Base):
  __tablename__ = 'professors'
  id = Column(String(50), primary_key=True)
  name = Column(Text)
  subject_id = Column(String(50))

class Students(Base):
  __tablename__ = 'students'
  id = Column(String(50), primary_key=True)
  name = Column(Text)
  department_id = Column(Integer)