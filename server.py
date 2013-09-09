# coding: utf-8
#
# Copyright (c) 2013 Tirith
#
# Licensed under the Apache License, Version 2.0 (the "License")
#
# Author: Thiago Ribeiro
# Email ribeiro dot it at gmail dot com
# Created: Aug 12, 2013, 10:27 PM
#
import os
import signal
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.locale

from controller import handlers
from lib.default import *
from lib.oid import *
from config import settings

if __name__ == '__main__':
	if settings.SERVER['log_enable']:
		logging.basicConfig(filename=settings.SERVER['log_path'], 
			level=logging.DEBUG)

	# load locale files
	tornado.locale.load_translations(settings.SERVER['lang_path'])

	print 'Sarting Server...'

	handlers = [
		(r'/accept?', AcceptHandler),
		(r'/associate?', AssociateHandler),
		(r'/authorize?', AuthorizeHandler),
		(r'/cancel?', CancelHandler),
		(r'/checkid_immediate?', CheckidImmediateHandler),
		(r'/checkid_setup?', CheckidSetupHandler),
		(r'/check_authentication?', CheckAuthenticationHandler),
		(r'/error?', ErrorHandler),
		(r'/id_res?', IdResHandller),
		(r'/login?', LoginHandler),
		(r'/logout?', LogoutHandler),
		(r'/test?', TestHandler),
		(r'/(.*)', BaseHandler),
	]
	
	application = tornado.web.Application(handlers, **settings.SERVER)

	application.listen(settings.SERVER['port'])
	signal.signal(signal.SIGINT, handle_signal)
	tornado.ioloop.IOLoop.instance().start()
