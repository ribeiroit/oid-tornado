# coding: utf-8
#
# Copyright (c) 2013 Tirith
#
# Licensed under the Apache License, Version 2.0 (the "License")
#
# Author: Thiago Ribeiro
# Email ribeiro dot it at gmail dot com
# Created: Aug 12, 2013, 10:17 PM
#
SERVER = {
	'log_enable': False,
	'log_path': '/var/log/oid/debug.log',

	'lang_path': './lang/',

	#'openid.assoc': 'HMAC-SHA1',
	'openid.assoc': 'HMAC-SHA256',

	'port': 8000,
}