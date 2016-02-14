# -*- coding:utf8 -*-
import re


def check_pw_strong(password):
    """
    密码强度检查
    """
    m = re.compile('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$') # 正则前项定界符，至少包涵一个数字、一个小写字母、一个大写字母

    if m.match(password):
        return True
    else:
        return False
