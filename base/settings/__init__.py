from . base import config

if config("IS_PRODUCTION", cast=bool, default=False):
    from . prod import *
else:
    from . dev import *
