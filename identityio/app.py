#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
identity.io
Author: Tim Henderson
Contact: tim.tadh@gmail.com, tadh@case.edu
Copyright: 2013 All Rights Reserved, see LICENSE
'''

import os, sys
from logging import getLogger
log = getLogger('identio')

from pyramid.config import Configurator
from pyramid.response import Response
from sqlalchemy import engine_from_config

from identityio.models import Base, DBSession


def hello_world(request):
    return Response('Hello')

def routes(config):
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    config.scan()

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    routes(config)
    app = config.make_wsgi_app()
    return app

