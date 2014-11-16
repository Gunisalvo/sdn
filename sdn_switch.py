#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from decorators import log
from pox.core import core

#@log
def launch(transparent=False):
	'''
	POX usará este método para iniciar o controlador
	'''

	core.registerNew(sdn_switch, str_to_bool(transparent))

class sdn_switch (object):

	@log
	def __init__ (self, transparent):
		core.openflow.addListeners(self)
		self.transparent = transparent
	@log
	def _handle_ConnectionUp (self, event):
		Controlador(event.connection, self.transparent)

class Controlador (object):
	@log
	def __init__ (self, connection, transparent):
		self.connection = connection
		self.transparent = transparent
		self.flow_table = {}
		connection.addListeners(self)

	@log
	def _handle_PacketIn (self, event):
		packet = event.parsed