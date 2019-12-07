
from flask import Blueprint
# 1，初始化蓝图
order_blu=Blueprint('order',__name__)

# 2，使用蓝图注册url上
@order_blu.route('/order/list')
def order_list():
    return 'orderlist'