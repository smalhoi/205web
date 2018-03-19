import os

from sqlalchemy import Column, String, Integer, ForeignKey, Text, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Skill(Base):

    __tablename__ = 'skill'

    id = Column(Integer, primary_key=True)
    skill_name = Column(String(64))


class Character(Base):

    __tablename__ = 'worker'

    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    education = Column(String(64))
    nationality = Column(String(64))
    married_status = Column(String(64))
    avatar = Column(String(64))
    skills = relationship(Skill, secondary='registrations', lazy='dynamic',
                          backref=backref('character', lazy='dynamic'))


class Registration(Base):

    __tablename__ = 'registrations'

    character_id = Column(Integer, ForeignKey('worker.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skill.id'), primary_key=True)


class Feedback(Base):

    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    phone = Column(String(64))
    email = Column(String(64))
    question = Column(Text)


# basedir = os.path.abspath(os.path.dirname(__file__))
# engine = create_engine(
#     'sqlite:///' + os.path.join(basedir, 'frog.sqlite'), echo=False)


# for mysql
engine = create_engine('mysql+mysqldb://root:root@localhost:3306/frog')
Session = sessionmaker(bind=engine)


session = Session()


def insert_data():

    c = Character()

    c.age = 25
    c.education = 'College'
    c.nationality = 'Nepali'
    c.married_status = 'Single'
    c.avatar = '1.png'

    for ab in ['HouseKeeping', 'Care of Pet', 'Care of Baby', 'Care of Bedridden']:
        a = Skill()
        a.skill_name = ab
        session.add(a)
        c.skills.append(a)

    session.add(c)
    session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # insert_data()
