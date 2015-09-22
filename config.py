#-*-coding:utf-8-*-

ACCESS_KEY = ''
SECRET_KEY = ''

BUCKET_NAME = ''
Q_DOMAIN = 'http(s)://xxxxxx.clouddn.com/' # your qiniu domain

CALLBACK_URL = 'http(s)://your_domain/doora/callback' # explained in http://docs.qiniu.com/api/v6/put.html#put-policy

PRIVATE_BUCKET = False # is your bucket public

TOKEN_EXPIRE = 3600 # upload token valid time, few minutes is enough
FILE_EXPIRE = 3600 # download token valid time, 3600 (1 hour) or more is highly recommended

try:
    from local_config import *
except:
    pass
