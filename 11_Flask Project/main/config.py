# Application 구동에 필요한 설정들
# EX) DB URI, Table, ...
# 적용 => Flask.config 인스턴스에 저장됨


# 디버그 모드 여부 설정값
DEBUG=True

# DB관련 설정값

import os
BASE_DIR=os.path.dirname(__file__)
DB_NAME='myapp.db'
DB_SQLITE_URI=f'sqlite:///{os.path.join(BASE_DIR,DB_NAME)}'

#DB_MYSQL_URI= 'mysql+pymysql://root:1234@localhost:3306/testdb'

DB_MARIA_URI='mariadb+mariadbconnector://root:root@127.0.0.1:3307/nai'

# ORM SQLALCHEMY에 연동할 RDDBMS 설정
SQLALCHEMY_DATABASE_URI = DB_MARIA_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False 