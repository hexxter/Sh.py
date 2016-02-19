import sys
from subprocess import Popen, PIPE


class Shell:
	def __init__(self, command, trusted, *args):

		assert command

		self._command = command
		self._args = []
		# print( self._args, args )
		self._args.extend(args)
		# print( self._args )
		self._trusted = trusted
		self._encoding = sys.getdefaultencoding()
		self._bufsize = 4096

	def _the_args_escaped(self):

		if (self._args):
			return " ".join("'" + it + "'" for it in self._args)
		else:
			return ""

	def _the_args(self):

		if (self._args):
			return " ".join(self._args)
		else:
			return ""

	def _the_command(self):

		if self._args:
			return self._command + " " + self._the_args()
		else:
			return self._command

	@property
	def run(self):

		with self.process() as proc:
			out = proc.stdout.read()
		# err = proc.stderr.read()

		outS = str(  out, self._encoding  )
		errS = ""  # str( err, self._encoding )

		return (outS, errS)

	def process(self, preproc=None):

		stdin = None
		stdout = PIPE
		stderr = None

		if preproc != None:
			stdin = preproc.stdout

		if hasattr(self, '_in'):
			stdin = PIPE

		proc = Popen(self._the_command(),
					 stdin=stdin, stdout=stdout, stderr=stderr,
					 bufsize=self._bufsize,
					 shell=True)

		if hasattr(self, '_in'):
			proc.stdin.write(self._in.encode(self._encoding))
			proc.stdin.close()

		if hasattr(self, '_out'):
			if hasattr(self._out, 'process'):
				subproc = self._out.process(proc)

				proc.stdout.close()

				return subproc

		return proc

	def arg(self, argument):

		self._args.append(argument)

		# print( self._args )

		return self

	def encoding(self, encoding):

		self._encoding = encoding

		return self

	def bufsize(self, newsize):

		self._bufsize = newsize

		return self

	def __str__(self):

		(out, err) = self.run

		return out

	def __repr__(self):

		return self._the_command()

	def __add__(self, other):

		return self.arg(other)

	def __ror__(self, other):

		# print( "=ROR=", type( other ), "|", self._command  )

		self._in = other

		return self

	def __or__(self, other):

		# print( "=OR=", self._command, type( other ) )

		if hasattr(other, '__call__'):

			# print( "==CALL==" )
			return other(self.__str__())

		else:

			if not hasattr(self, '_out '):
				# print( "==STORE==" )
				self._out = other
			else:
				if hasattr(self._out, '__or__'):
					# print( "==STORE==" )
					self._out.__or__(other)
				else:
					raise AttributeError('Tried to chain the unchainable')

			return self


class Sh(Shell):
	# "Execute Shell commands in a insane way"

	def __init__(self, command, *args):
		super(Sh, self).__init__(command, trusted=False, *args )


class sh(Shell):
	# "Execute Shell commands in a sane way"

	def __init__(self, command, *args):
		super(sh, self).__init__(command, trusted=True, *args )
