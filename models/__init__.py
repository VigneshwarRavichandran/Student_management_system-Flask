from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey, String, Text, DateTime
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:1998@localhost/student_management",echo = True)
Base = declarative_base()
session = Session(engine)

class College(Base):
  __tablename__ = 'college'
  id = Column(Integer, primary_key=True, nullable=False)
  name = Column(String(50), nullable=False) 
  location = Column(Text, nullable=False)

class Departments(Base):
  __tablename__ = 'departments'
  id = Column(Integer, primary_key=True, nullable=False)
  name = Column(String(50), nullable=False)

class Subjects(Base):
  __tablename__ = 'subjects'
  id = Column(String(50), primary_key=True, nullable=False)
  name = Column(Text, nullable=False)
  department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)
  department = relationship("Departments", foreign_keys=[department_id])

class Users(Base):
  __tablename__ = 'users'
  id = Column(String(50), primary_key=True, nullable=False)
  encrypted_data = Column(Text, nullable=False)

class Professors(Base):
  __tablename__ = 'professors'
  id = Column(String(50), primary_key=True, nullable=False)
  name = Column(Text, nullable=False)
  subject_id = Column(String(50), ForeignKey('subjects.id'), nullable=False)
  subject = relationship("Subjects", foreign_keys=[subject_id])

class Students(Base):
  __tablename__ = 'students'
  id = Column(String(50), primary_key=True, nullable=False)
  name = Column(Text, nullable=False)
  department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)
  department = relationship("Departments", foreign_keys=[department_id])