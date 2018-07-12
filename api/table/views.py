# -*- coding: utf-8 -*-

"""
api.table.views
~~~~~~~~~~~~~~~~~
模型创建API
"""

from flask import Blueprint
from api import database

table = Blueprint('table', __name__)


@table.route("/")
def home_page():
    online_users = database.db.users.find({"online": True})
    print(online_users)
