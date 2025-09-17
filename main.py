from sqlalchemy import insert, select, update, delete

from database import engine, metadata
from models import users, tasks

metadata.create_all(engine)

def create_user():
    with engine.connect() as conn:
        stmt = insert(users).values(username="vali", fullname="ali")
        conn.execute(stmt)
        conn.commit()

def create_task(user_id: int):
    with engine.connect() as conn:
        stmt = insert(tasks).values(name="kitob oqish", user_id=user_id)
        conn.execute(stmt)
        conn.commit()

def get_users():
    with engine.connect() as conn:
        stmt = select(users)
        rows = conn.execute(stmt)

        for row in rows:
            print(row)

def get_tasks(user_id: int):
    with engine.connect() as conn:
        stmt = select(tasks).where(tasks.c.user_id==user_id)
        rows = conn.execute(stmt)

        for row in rows:
            print(row)

def update_user(user_id: int):
    with engine.connect() as conn:
        stmt = select(users).where(users.c.id==user_id)
        result = conn.execute(stmt)
        
        if list(result):
            stmt = update(users).where(users.c.id==user_id).values(username='updated username')
            conn.execute(stmt)
            conn.commit()
        else:
            print('user mavjud emas')

def delete_user(user_id: int):
    with engine.connect() as conn:
        stmt = select(users).where(users.c.id==user_id)
        result = conn.execute(stmt)
        
        if list(result):
            stmt = delete(users).where(users.c.id==user_id)
            conn.execute(stmt)
            conn.commit()
        else:
            print('user mavjud emas')

def main():
    # create_user()
    # create_task(1)
    # get_users()
    # get_tasks(2)
    # update_user(1)
    delete_user(1)

if __name__ == "__main__":
    main()
