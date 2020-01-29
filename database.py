from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# replace lecture.db with your own database file
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(username, email, password, birthdate, gender, bio):
	user_object=User(
		username = username,
		email = email,
		password = password, 
		birthdate = birthdate,
		gender = gender,
		bio = bio)
	session.add(user_object)
	session.commit()
# add_user("Noor", "noor.m.ali2003@gmail.com", "noor123", "12/10/2003","female", "hi")

def update_bio(username,bio):
	user_object = session.query(User).filter_by(username=username).first()
	user_object.bio = bio 
	session.commit()
# update_bio("Noor", "hello")

def delete_user(username):
	session.query(User).filter_by(username=username).delete()
	session.commit()
# delete_user("")

def query_all():
	users=session.query(User).all()
	return users
# print(query_all())

def query_user(username, password):
	user = session.query(User).filter_by(username=username).first()
	if user:
		if password == user.password:
			return True
	else:
		return False

def query_one(username):
	user = session.query(User).filter_by(username=username).first()
	return user
