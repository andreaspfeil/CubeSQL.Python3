import hashlib
import json
import random
import base64
import socket
import binascii

def sha1( data, binary = False ):
	if binary:
		return hashlib.sha1( data ).digest()
	else:
		return hashlib.sha1( data ).hexdigest()

class CubeSQL:
	def __init__(self, host, name, password ):
		self.socket = None
		self.socketTimeout = 12
		if self.open( host, name, password ) == False:
			raise "Connection error" 
	
	def resetError( self ):
		self.errorCode = 0
		self.errorMessage = ""
		
	def isError( self ):
		return self.errorCode != 0
	
	def sendRequest( self, json_request ):
		if self.socket != None:
			try:
				self.resetError()
				#print( "->" + json_request )
				data = self.socket.sendall( json_request )
				data = self.socket.recv( 1024 )
				#print( "<- " + data )
				
				try:
					data = json.loads( data )
					if "errorCode" in data:
						self.errorCode = data[ "errorCode" ]
					if "errorMsg" in data:
						self.errorMessage = data[ "errorMsg" ]
					return data
					
				except json.decoder.JSONDecodeError:
					self.errorCode = -1
					self.errorMessage = json.decoder.JSONDecodeError.msg
					
			except OSError:
				self.errorCode = OSError.errno
				self.errorMessage = OSError.strerror
				
		self.errorCode = -1
		self.errorMessage = "Socket error"
	
	def disconnect( self ):
		if self.socket != None:
			request = { "command": "DISCONNECT" }
			json_request = json.dumps( request )
			try:
				self.sendRequest( json_request )
				self.socket.close()
				self.socket = None
			except (socket.error, msg):
				self.errorCode = socket.error
				self.errorMessage = msg
	
	def connect( self, host, port = 4430, timeOut = 12 ):
		try:	
			self.disconnect()
			self.socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
			self.socket.connect(( host, port ))
			return True
		except (socket.error, msg):
			print( msg )
			self.errorCode = socket.error
			self.errorMessage = msg
			return False
		
	def open( self, host, username, password ):
		if self.connect( host ) == True:
			randpool = str( random.random() )[2:12]
			username = sha1( str( randpool + username ).encode( 'utf-8' ) )
			password = sha1( password.encode( 'utf-8' ), True )
			password = sha1( password, True )
			password = base64.b64encode( password )
			password = randpool + str( password )
			password = sha1( password.encode( 'utf-8' ) )
			request = { "command": "CONNECT", "username": username, "password": password, "randpool": randpool }
			json_request = json.dumps( request, sort_keys = True )			
			self.sendRequest( json_request )
				
		return self.isError() == False
	
	def execute( self, sql ):
		request = { "command": "EXECUTE", "sql": sql }
		json_request = json.dumps( request )
		self.sendRequest( json_request )
		return self.isError() == False
	
	def select( self, query ):
		request = { "command": "SELECT", "sql": query }
		json_request = json.dumps( request )
		data = self.sendRequest( json_request )
		if self.isError():
			return None
		return data
				
	def use( self, database ):
		return self.execute( "USE DATABASE " + database + ";" )