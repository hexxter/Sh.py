#!/usr/bin/python3

from Sh import Sh,sh

"""
This is how it should work
Note that we use operator overloading for | and __str__ and command
chaining in order to get a cleaner syntax. 
"""

"""
Nomal shell operation with pipes and no hustles
"""
print( "Inline pipe" )
result = Sh( "ls / | grep bin" )
print( result )

"""
Pipe a String in the shell pipe. This is nice and a must have!!22!
"""
print( "string to pipe" )
result = "blah" | Sh( "sed -e 's/ah/ub/'" )
print( result )

"""
Pipe into function.
I don't know if this could work or even is a good idea
"""
print( "pipe to function" )
Sh( "ls /" ) | print

print( "Adding args" )
result = Sh( "ls" ).arg( "-a" ).arg( "/" )
print( result )

