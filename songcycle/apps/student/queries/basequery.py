# import area
from collections import namedtuple
import threading

# CRUDのRは、ここに集約する。

class BaseQuery:

    def namedtuplefetchall(self, cursor):
        "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    def to_with_param_sql(self, sql, param_disctionary):

        for key in param_disctionary.keys():
            sql = sql.replace('@' + key, param_disctionary[key])

        return sql
    
    def to_like_value(self, value):
        return "'%" + value + "%'"