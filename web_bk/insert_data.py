from model import Character, Skill, Session


session = Session()


def insert_data():

    n = int(input('Number of new domestic helper\n>'))
    for i in range(n):
        c = Character()

        c.age = int(input('Age of the helper:\n>'))
        c.education = input('Education of the helper:\n>')
        c.nationality = input('Nationality of the helper:\n>')
        c.married_status = input('Married status of the helper:\n>')
        c.avatar = input('The image file name of the helper(example: 1.png):\n>')

        skills = input('Abilities of the helper(Please use comma in between to separate the skills):\n>').split(r',')
        for ab in skills:
            a = Skill()
            a.skill_name = ab
            session.add(a)
            c.skills.append(a)

        session.add(c)
        try:
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()


if __name__ == '__main__':
    insert_data()
