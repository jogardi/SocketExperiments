from twisted.internet import protocol, reactor, endpoints

class Echo(protocol.Protocol):
    def connectionMade(self):
        print(f'connection made to {self.transport.getPeer()}')
    
    def dataReceived(self, data):
        print("data received")
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

endpoints.serverFromString(reactor, "tcp:8000").listen(EchoFactory())
print("before starts")
reactor.run()
print('started running')