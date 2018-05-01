from jsonkv import JsonKV
from datetime import datetime


db = JsonKV('test.json')

with db:
    db['a'] = 'a'
    db['now'] = datetime.now()