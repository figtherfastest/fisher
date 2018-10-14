# 所有web蓝图相关的额文件都会放在这个文件
from flask import Blueprint

web = Blueprint('web',__name__)

from app.web import book