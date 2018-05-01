# coding: utf-8

import json
from copy import deepcopy
import os
from datetime import date, datetime


class JsonKV(object):
    def __init__(self, path: str, mode: str = 'r+'):
        self.path = path
        self.mode = mode
        self.data = {}

    def __enter__(self):
        if not os.path.isfile(self.path):
            open(self.path, 'w').close()

        self.f = open(self.path, self.mode)
        try:
            content = self.f.read()
            self.data = json.loads(content)
        except json.decoder.JSONDecodeError as e:
            print('Warning: {}'.format(e))
        self.origin_data = deepcopy(self.data)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save()
        self.f.close()

    def __getitem__(self, item):
        if item in self.data:
            return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        return dict.__iter__(self.data)

    def save(self, indent=None):
        if self.f.writable():
            self.f.seek(0)
            self.f.write(json.dumps(self.data, ensure_ascii=False, indent=indent, default=self.json_serial))

    def restore(self):
        self.data = deepcopy(self.origin_data)

    @staticmethod
    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %X')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')

        raise TypeError("Type %s not serializable" % type(obj))
