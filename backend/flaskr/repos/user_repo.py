from .. import get_db

TABLE_NAME = 'users'

class UserRepo:
    def __init__(self, db=None):
        if db is None:
            self.db = get_db()
        else:
            self.db = db

    def get(self, username):
        return self.db.execute(
            f'SELECT * FROM {TABLE_NAME} WHERE username = ?', (username,)
        ).fetchone()

    def create(self, username, password, email, first_name, last_name):
        db = self.db
        db.execute(
            f'INSERT INTO {TABLE_NAME} (username, password, email, first_name, last_name) VALUES (?, ?, ?, ?, ?)',
            (username, password, email, first_name, last_name)
        )
        db.commit()

    def update(self, username, password, email, first_name, last_name):
        db = self.db
        db.execute(
            f'UPDATE {TABLE_NAME} SET password = ?, email = ?, first_name = ?, last_name = ? WHERE username = ?',
            (password, email, first_name, last_name, username)
        )
        db.commit()

    def delete(self, username):
        db = self.db
        db.execute(
            f'DELETE FROM {TABLE_NAME} WHERE username = ?', (username,)
        )
        db.commit()
