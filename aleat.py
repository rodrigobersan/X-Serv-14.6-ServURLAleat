#!/usr/bin/python
import webapp
import random
import socket


class randomServer(webapp.webApp):
	def process(self, parsedRequest):
		nextExt = str(random.randint(0,100000))
		nextURL = "http://localhost:1234/" + nextExt
		msg = "<h1>Hola. " + '<a href="' + nextURL + '">' + "Quieres mas?" + "</a>" + "</h1>"

		return("200 OK", "<html><body>" + msg + "</html></body>")

if __name__ == "__main__":
	Server = randomServer("localhost", 1234)
