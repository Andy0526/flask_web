# -*- coding: utf-8 -*-
from werkzeug.contrib.fixers import ProxyFix

from .app import create_app

__all__ = ['app']

app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)
