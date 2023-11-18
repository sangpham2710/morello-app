from . import get_db

TABLE_NAME = 'collection_sessions'

class SessionRepo:
    def __init__(self, db=None):
        if db is None:
            self.db = get_db()
        else:
            self.db = db

    def create(self, name, group_name, group_creator, date_created=None):
        db = get_db()
        db.execute(
            f'INSERT INTO {TABLE_NAME} (name, group_name, group_creator, date_created) VALUES (?, ?, ?, ?)',
            (name, group_name, group_creator, date_created)
        )
        db.commit()
    
    def get_all(self):
        db = get_db()
        sessions = db.execute(
            f'SELECT * FROM {TABLE_NAME}'
        ).fetchall()
        return sessions

    def update(self, name, group_name, group_creator, date_created):
        db = get_db()
        db.execute(
            f'UPDATE {TABLE_NAME} SET group_name = ?, group_creator = ?, date_created = ? WHERE name = ?',
            (group_name, group_creator, date_created, name)
        )
        db.commit()

    def delete(self, name):
        db = get_db()
        db.execute(
            f'DELETE FROM {TABLE_NAME} WHERE name = ?',
            (name,)
        )
        db.commit()
