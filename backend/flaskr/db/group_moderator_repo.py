from . import get_db

TABLE_NAME = 'group_moderators'

class GroupModeratorRepo:
    def __init__(self, db=None):
        if db is None:
            self.db = get_db()
        else:
            self.db = db

    def create(self, group_name, group_creator, moderator_username, date_joined=None):
        db = self.db
        db.execute(
            f'INSERT INTO {TABLE_NAME} (group_name, group_creator, moderator_username, date_joined) VALUES (?, ?, ?, ?)',
            (group_name, group_creator, moderator_username, date_joined)
        )
        db.commit()

    def get_all(self):
        db = self.db
        group_moderators = db.execute(
            'SELECT * FROM group_moderator'
        ).fetchall()
        return group_moderators

    def get_by_group_name(self, group_name):
        db = self.db
        group_moderators = db.execute(
            'SELECT * FROM group_moderator WHERE group_name = ?', (group_name,)
        ).fetchall()
        return group_moderators

    def get_by_moderator_username(self, moderator_username):
        db = self.db
        group_moderators = db.execute(
            'SELECT * FROM group_moderator WHERE moderator_username = ?', (moderator_username,)
        ).fetchall()
        return group_moderators

    def get_by_group_name_and_moderator_username(self, group_name, moderator_username):
        db = self.db
        group_moderators = db.execute(
            'SELECT * FROM group_moderator WHERE group_name = ? AND moderator_username = ?', (group_name, moderator_username)
        ).fetchall()
        return group_moderators

    def update(self, group_name, moderator_username, date_joined):
        db = self.db
        db.execute(
            'UPDATE group_moderator SET date_joined = ? WHERE group_name = ? AND moderator_username = ?',
            (date_joined, group_name, moderator_username)
        )
        db.commit()

    def delete(self, group_name, moderator_username):
        db = self.db
        db.execute(
            'DELETE FROM group_moderator WHERE group_name = ? AND moderator_username = ?',
            (group_name, moderator_username)
        )
        db.commit()
