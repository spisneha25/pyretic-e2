##########################################################
# Computer Networks course project, CS6250, Georgia Tech #
##########################################################

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class Simple_topo(Topo):
    """
    A simple example topology class

            ----
            |H1|
            ----
             |
            ----
            |s1|
            ----
             |
      +------+------+
      |             |
    ----           ----
    |s4|           |s3|
    ----           ----
      |             |
      +------+------+
             |
            ----
            |s5|
            ----
             |
            ----
            |s2|
            ----
             |
            ----
            |H2|
            ----
    """
    def __init__(self):

        Topo.__init__( self )
        ###adding switches and hosts
        H1 = self.addHost('h1')
        H2 = self.addHost('h2')
        Sw1 = self.addSwtich('s1')
        Sw2 = self.addSwtich('s2')
        Sw3 = self.addSwtich('s3')
        Sw4 = self.addSwtich('s4')
        Sw5 = self.addSwtich('s5')
        self.addLink( H1, Sw1 )
        self.addLink( H2, Sw2 )
        self.addLink( Sw1, Sw3 )
        self.addLink( Sw3, Sw5 )
        self.addLink( Sw1, Sw4 )
        self.addLink( Sw4, Sw5 )
        self.addLink( Sw5, Sw2 )

##creating a mininet class
net = Mininet( topo = Simple_topo, controller=lambda name: RemoteController( name='c0', ip='127.0.0.1',port=6633) )
##strt and stop
net.start()
CLI(net)
net.stop()
