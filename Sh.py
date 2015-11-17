#!/usr/bin/python3

from subprocess import Popen, PIPE
import sys

class Shell:

	def __init__( self, command, *args, trusted ):

		assert command

		self._command = command
		self._args = args
		self._trusted = trusted
		self._encoding = sys.getdefaultencoding()
		self._bufsize = 4096


	def run( self ):

		if not self._trusted:

			stdin = PIPE
			stdout = PIPE
			stderr = PIPE

			with Popen( self._command,
					stdin=stdin, stdout=stdout, stderr=stderr,
					bufsize=self._bufsize,
					shell=True
			) as proc:

				out = proc.stdout.read()
				err = proc.stderr.read()

		else:

			with Popen( self._command, stdin=PIPE, stdout=PIPE, stderr=PIPE ) as proc:

				out = proc.stdout.read()
				err = proc.stderr.read()

		outS = out.decode( self._encoding )
		errS = err.decode( self._encoding )

		return (outS, errS)


	def arg( self, argument ):

		self._command += " " + argument;

		return self


	def encoding( self, encoding ):

		self._encoding = encoding

		return self


	def bufsize( self, newsize ):

		self._bufsize = newsize

		return self


	def __str__( self ):

		(out,err) = self.run()

		return out;


	def __add__( self, other ):

		self._command += " " + other


	def __ror__( self, other ):

		print( "ROR" )
		print( type( other ) )
		#print( dir( other ) )

		self._in = other

		return self


	def __or__( self, other ):

		print( "OR" )
		print( isinstance( other, function ) )
		print( type( other ) )
		#print( dir( other ) )

		self._out = other

		return self;


class Sh( Shell ):

	"Execute Shell commands in a insane way"

	def __init__( self, command, *args ):

		super( Sh, self ).__init__( command, args, trusted=False )


class sh( Shell ):

	"Execute Shell commands in a sane way"

	def __init__( self, command, *args ):

		super( Sh, self ).__init__( command, args, trusted=True )

