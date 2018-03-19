from model import Character, Skill, Session


session = Session()


test = session.query(Character).filter_by(id=1).first()

session.delete(test)
session.commit()
