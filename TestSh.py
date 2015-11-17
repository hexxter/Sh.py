#!/usr/bin/python3

import unittest
import sys
from Sh import Sh,sh


class TestSh(unittest.TestCase):

	"""
	This is how it should work
	Note that we use operator overloading for | and __str__ and command
	chaining in order to get a cleaner syntax. 
	"""

	def setUp( self ):
		pass


	def test_long_pipe( self ):

		return#

		"blah" | Sh( "sed -e 's/ah/ub/'" ) | Sh( "tr '[:lower:]' '[:upper:]'" ) | print


	def test_normal( self ):

		return

		"""
		Nomal shell operation with pipes and no hustles
		"""
		
		print( "=== Inline pipe ===" )

		result = str( Sh( "ls . | grep ^Sh.py" ) )
		print( result )
		self.assertEqual( ""+result, "Sh.py\n")

	
	def test_piping( self ):

		return

		"""
		This is (only) needed if we want to use secure scripting
		"""

		print( "=== Extern pipe ===" )

		result = str( Sh( "ls", "." ) | Sh( "grep", "^Sh.py" ) )
		print( result )
		self.assertEqual( ""+result, "Sh.py\n")

	
	def test_string_pipe( self ):

		return#

		"""
		Pipe a String in the shell pipe. This is nice and a must have!!22!
		"""

		print( "=== string to pipe ===" )

		result = "blah" | Sh( "sed -e 's/ah/ub/'" )
		print( result )
		self.assertEqual( str( result ), "blub" )

		#result = "blah" | Sh( "sed", "-e", "'s/ah/ub/'" )
		#print( result )
		#self.assertEqual( str( result ), "blub" )


	def inner_printer( self, arg ):

		print( arg )

		self._last_message = 'blah'


	def test_pipe_func( self ):

		return#

		"""
		Pipe into function.
		I don't know if this could work or even is a good idea
		"""

		print( "=== pipe to function ===" )

		Sh( "echo 'blah'" ) | printer

		Sh( "echo 'blah'" ) | self.inner_printer

		self.assertEqual( self._last_message, 'blah' )


	def test_arg_chaining( self ):

		print( "=== Adding args ===" )

		shell = Sh( "ls" ).arg( "-a" ).arg( "." )

		self.assertEqual( shell.info(), 'ls -a .' )


def printer( arg ):

    print( arg )


if __name__ == '__main__':

	unittest.main()
