from .. import get_db

TABLE_NAME = 'collect_session_entries'

class SessionEntryRepo:
    def create(self, session_name, session_group_name, session_group_creator, member_name):
        db = get_db()
        db.execute(
            f'INSERT INTO {TABLE_NAME} (group_name, group_creator, session_name, member) VALUES (?, ?, ?, ?, ?)',
            (session_group_name, session_group_creator, session_name, member_name)
        )
        db.commit()
