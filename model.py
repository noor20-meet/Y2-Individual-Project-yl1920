from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	username = Column(String, primary_key=True)
	email = Column(String)
	password = Column(String)
	birthdate= Column(String)
	gender=Column(String)
	bio=Column(String)

	def __repr__(self):
		# return str(self.__dict__)
		return str([self.username, self.email, self.password,self.birthdate,self.gender, self.bio])

