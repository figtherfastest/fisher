
from . import web


@web.route('/')
def index():
   return 'main'

@web.route('/personal/')
def personal_center():
   pass