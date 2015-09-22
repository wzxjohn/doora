#-*-coding:utf-8-*-

from config import ACCESS_KEY, SECRET_KEY

from qiniu import Auth

q = Auth(ACCESS_KEY, SECRET_KEY)
