def setup_db_for_test():
    import os
    import sqlite3
    db = sqlite3.connect(':memory:')
    with open(os.path.join(os.path.dirname(__file__), '..', 'schema.sql')) as f:
        db.executescript(f.read())
    return db
