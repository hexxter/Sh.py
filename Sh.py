#!/usr/bin/python3

from subprocess import Popen, PIPE

class Shell:

    def __init__( self, command, secure ):

        assert command

        self._command = command
        self._secure = False
        self._encoding="utf-8"


    def run( self ):

        if( not self._secure ):
        
            with Popen( self._command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True ) as proc:

                out = proc.stdout.read()
                err = proc.stderr.read()

        else:

            with Popen( self._command, stdin=PIPE, stdout=PIPE, stderr=PIPE ) as proc:

                out = proc.stdout.read()
                err = proc.stderr.read()

        if( out ):
            out = out.decode( "utf-8" )
        if( err ):
            err = out.decode( "utf-8" )

        return (out, err)


    def arg( self, argument ):

        self._command += " " + argument;

        return self


    def encoding( self, encoding ):

        self._encoding = encoding

        return self


    def __str__( self ):

        (out,err) = self.run()

        return out;


    def __add__( self, other ):
        
        self._command += " " + other


    def __ror__( self, other ):

        print( dir( other ) )

        self._in = other

        return self


    def __or__( self, other ):

        print( dir( other ) )

        self._out = other

        return self;


class Sh( Shell ):

    "Execute Shell commands in a insane way"

    def __init__( self, command ):

        super( Sh, self ).__init__( command, False )


class sh( Shell ):

    "Execute Shell commands in a sane way"

    def __init__( self, command ):

        super( Sh, self ).__init__( command, True )

