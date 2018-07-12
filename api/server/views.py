from flask import Blueprint
from api.server import views

server = Blueprint('server', __name__)


@server.route('/stats', methods=['GET', ])
def stats():
    # 返回服务器状态
    pass
