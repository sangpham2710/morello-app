import os
import sqlite3

from . import setup_db_for_test
from ..user_repo import UserRepo

def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5

def test_user_repo():
    db = setup_db_for_test()
    UserRepo(db).create('test', 'test', 'test', 'test', 'test')
    assert UserRepo(db).get('test')[:4] == ('test', 'test', 'test', 'test')
