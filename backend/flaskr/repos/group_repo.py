from .. import get_db

class GroupRepo:
    def get_all(self):
        return get_db().execute(
            'SELECT * FROM groups'
        ).fetchall()

    def get(self, group_name, creator):
        return get_db().execute(
            'SELECT * FROM groups WHERE group_name = ? AND creator = ?', (group_name, creator)
        ).fetchone()

    def create(self, group_name, creator, description=None, date_created=None):
        db = get_db()
        db.execute(
            'INSERT INTO groups (group_name, creator, description, date_created) VALUES (?, ?, ?, ?)',
            (group_name, creator, description, date_created)
        )
        db.commit()

    def update(self, group_name, creator, description=None, date_created=None):
        db = get_db()
        db.execute(
            'UPDATE groups SET description = ?, date_created = ? WHERE group_name = ? AND creator = ?',
            (description, date_created, group_name, creator)
        )
        db.commit()

    def delete(self, group_name, creator):
        db = get_db()
        db.execute(
            'DELETE FROM groups WHERE group_name = ? AND creator = ?', (group_name, creator)
        )
        db.commit()
