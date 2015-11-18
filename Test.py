#!/usr/bin/python3

import unittest
from sh.Sh import Sh,sh


class TestSh(unittest.TestCase):

	"""
	This is how it should work
	Note that we use operator overloading for | and __str__ and command
	chaining in order to get a cleaner syntax. 
	"""

	def setUp( self ):
		pass

	
	def test_str__( self ):

		expr = Sh( "echo foo" )

		print( expr )

		self.assertNotEqual( expr, "foo\n" ) #because this doesn't run it
		self.assertEqual( str( expr ), "foo\n" ) #This will run it

		self.assertEqual( repr( expr ), "echo foo" ) 


	def test_long_pipe( self ):

		"blah" | Sh( "sed -e 's/ah/ub/'" ) | Sh( "tr '[:lower:]' '[:upper:]'" ) | print


	def test_normal( self ):

		"""
		Inline pipe
		Nomal shell operation with pipes and no hustles
		"""
		
		result = str( Sh( "echo foo | sed -e 's/foo/bar/'" ) )
		#print( result )
		self.assertEqual( ""+result, "bar\n")

	
	def test_piping( self ):

		"""
		External pipe
		The external pipe is (only) needed if we want to use secure scripting
		"""

		result = str( Sh( "echo foo" ) | Sh( "sed -e 's/foo/bar/'" ) )
		#print( result )
		self.assertEqual( result, "bar\n")

	
	def test_string_pipe( self ):

		"""
		String to Pipe
		Pipe a String in the shell pipe. This is nice and a must have!!22!
		"""

		result = "blah" | Sh( "sed -e 's/ah/ub/'" )
		#print( result )
		self.assertEqual( str( result ), "blub" )

		result = "blah" | Sh( "sed", "-e", "'s/ah/ub/'" )
		print( result )
		self.assertEqual( str( result ), "blub" )


	def inner_printer( self, arg ):

		print( arg )

		self._last_message = 'blah'


	def test_pipe_func( self ):

		"""
		Pipe to Function.
		I don't know if this could work or even is a good idea
		"""

		Sh( "echo 'blah'" ) | printer

		Sh( "echo 'blah'" ) | self.inner_printer

		self.assertEqual( self._last_message, 'blah' )


	def test_arg_chaining( self ):

		"""
		Adding Args
		"""

		shell = Sh( "echo" ).arg( "foo" ).arg( "bar" )

		self.assertEqual( repr( shell ), 'echo foo bar' )

		shell += "faz"

		self.assertEqual( repr( shell ), 'echo foo bar faz' )


def printer( arg ):

	print( arg )


if __name__ == '__main__':

	unittest.main()

