# -*- coding: utf-8 -*-

"""
runserver.py
~~~~~~~~~~~~~~~~~
fowan-server 启动脚本
"""

from api import app
# see https://stackoverflow.com/questions/42639466/importing-from-init-in-flask
# views using database ,so import after database init
from api.admin.views import admin
from api.apps.views import apps
from api.auth.views import auth
from api.db.views import db
from api.develop.views import develop
from api.email.views import email
from api.file.views import file
from api.server.views import server
from api.sms.views import sms
from api.table.views import table
# register all blueprint
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(apps, url_prefix='/apps')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(db, url_prefix='/db')
app.register_blueprint(develop, url_prefix='/develop')
app.register_blueprint(email, url_prefix='/email')
app.register_blueprint(file, url_prefix='/file')
app.register_blueprint(server, url_prefix='/server')
app.register_blueprint(sms, url_prefix='/sms')
app.register_blueprint(table, url_prefix='/table')

if __name__ == '__main__':
    app.debug = True
    app.run()
