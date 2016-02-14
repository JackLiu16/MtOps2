# -*- coding:utf8 -*-
import requests


class MtDbApi(object):
    """
    美图数据库 API for Python
    """
    __root_uri = 'http://192.168.7.29:10060/'
    __auth_user = 'db_mtops'
    __auth_token = 'yZGLRu9p'
    
    def __init__(self, action):
        self.request_url = self.__root_uri + action

    def __post(self, url, data):
        try:
            response = requests.post(url, data)
            response.raise_for_status() # 状态码非 200 抛出异常
            result = response.json()
        except requests.RequestException as e:
            result = {'exception': u"Http Error, %s" %e}
        return result

    def ct_check(self, host, port, db_name, sql):
        """
        Mt 数据库普通建表预检测
        """
        data = {
            '_auth_user': self.__auth_user, '_auth_token': self.__auth_token,
            'host': host, 'port': port, 'db': db_name, 'sql': sql
        }
        return self.__post(self.request_url, data)
