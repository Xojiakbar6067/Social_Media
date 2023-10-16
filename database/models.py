from sqlalchemy import Integer, DateTime, Date, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

#tablitsa polzovatelya

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    city = Column(String)
    birthday = Column(Date)
    profile_photo = Column(String)

    reg_date = Column(DateTime)


#tablitsa publikatsii

class UserPost(Base):
    __tablename__ = 'user_posts'
    post_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    post_text = Column(String)
    likes = Column(Integer, default=0)

    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')

#tablitsa fotografii k postu

class PostPhoto(Base):
    __tablename__ = 'post_photo'
    photo_id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('user_posts.post_id'))
    photo_path = Column(String)

    photo_fk = relationship(UserPost, lazy='subquery')

#tablitsiya komentariy

class PostComment(Base):
    __tablename__ = 'post_comments'
    comment_id = Column(Integer, autoincrement=True, primary_key=True)

    post_id = Column(Integer, ForeignKey('user_posts.post_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))

    comment_text = Column(String)
    publish_date = Column(DateTime)

    post_fk = relationship(User, lazy='subquery')
    post_fk = relationship(UserPost, lazy='subquery')
