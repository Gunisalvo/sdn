#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
from functools import wraps

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",filename="sdn.log",level=logging.DEBUG)

def log(func):
	@wraps(func)
	def log_wrapper(self, *arg, **keyargs):
		try:
			logging.debug("calling: " + func.func_name)
			print "calling: " + func.func_name
			result = func(self, *arg, **keyargs)
			return result
		except Exception as ex:
			logging.warn(func.func_name + (": %s" % ex))
			print func.func_name + (": %s" % ex)
			raise ex
	return log_wrapper
