# import area
from collections import namedtuple
from django.db import connection

# CRUDのRは、ここに集約する。


class BaseQuery:

    __not_value_keywords = ['sort', 'desc', 'limit', 'offset']

    def namedtuplefetchall(self, cursor):
        "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    def fetchone(self, sql, param_list):

        sql, param_values = self.__preparation(sql, param_list)

        with connection.cursor() as cursor:
            cursor.execute(sql, param_values)
            result = cursor.fetchone()

        return result

    def fetchall(self, sql, param_list):

        sql, param_values = self.__preparation(sql, param_list)

        with connection.cursor() as cursor:
            cursor.execute(sql, param_values)
            result_data = self.namedtuplefetchall(cursor)

        return result_data

    def __preparation(self, sql, param_list):

        param_values = []
        for param in param_list:
            for key in param.keys():
                if (key in self.__not_value_keywords):
                    sql = sql.replace('@' + key, param[key])
                else:
                    sql = sql.replace('@' + key, '%s')
                    param_values.append(param[key])

        return sql, param_values

    def to_like_value(self, value):
        return "%" + value + "%"

    def _str_to_bool(self, value):
        if(value == "True"):
            return True
        return False
