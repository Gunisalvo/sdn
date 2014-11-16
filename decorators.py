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
			result = func(self, *arg, **keyargs)
			return result
		except Exception as ex:
			logging.warn(func.func_name + (": %s" % ex))
			raise ex
	return log_wrapper

class Cobaia(object):

	def __init__(self):
		self.name = "John"
		self.family = "Doe"
	@log
	def get_fullname(self):
		raise IOError("pau!")
		return self.name+" "+self.family

my_person = Cobaia()
print my_person.get_fullname()
