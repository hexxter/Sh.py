#!/usr/bin/python3

from Sh import Sh,sh

import unittest
import logging, sys

class TestSh(unittest.TestCase):
	"""
	This is how it should work
	Note that we use operator overloading for | and __str__ and command
	chaining in order to get a cleaner syntax. 
	"""

	def setUp(self):
		pass

	def test_normal(self):
		"""
		Nomal shell operation with pipes and no hustles
		"""
		
		log.info( "Inline pipe" )
		result = Sh( "ls / | grep bin" )
		#log.info( result )
		self.assertEqual( str(result), "bin\nsbin\n")
	
	def test_string_pipe(self):
		"""
		Pipe a String in the shell pipe. This is nice and a must have!!22!
		"""
		
		log.info( "string to pipe" )
		result = "blah" | Sh( "sed -e 's/ah/ub/'" )
		#log.info( result )

	def test_pipe_func(self):
		"""
		Pipe into function.
		I don't know if this could work or even is a good idea
		"""
		pass
		#log.info( "pipe to function" )
		#Sh( "ls /" ) | print

		#log.info( "Adding args" )
		#result = Sh( "ls" ).arg( "-a" ).arg( "/" )
		#log.info( result )

if __name__ == '__main__':
	
	log = logging.getLogger("TestSh")
	log.setLevel(logging.DEBUG)
	unittest.main()
