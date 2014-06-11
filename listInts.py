#!/usr/bin/python

from jsonrpclib import Server
import pprint

switch = Server( "https://arista:arista@10.10.10.11/command-api" )

response = switch.runCmds( 1, ["show interfaces description"] )

#print "The switch's system MAC addess is", response[0]["systemMacAddress"]

#pp = pprint.PrettyPrinter()
#pp.pprint(response[0])
pprint.pprint(response[0])


print "The switch's system Management description is '{0}'".format(response[0]["interfaceDescriptions"]["Management1"]["description"])
