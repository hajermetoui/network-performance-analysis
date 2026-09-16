from mininet.net import Mininet
from mininet.node import OVSBridge
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
def build_network():
	net = Mininet(switch=OVSBridge, link=TCLink )
	h1= net.addHost('h1')
	h2= net.addHost('h2')
	h3= net.addHost('h3')
	h4= net.addHost('h4')
	s1= net.addSwitch('s1')
	s2= net.addSwitch('s2')
	net.addLink(h1, s1)
	net.addLink(h2 , s1)
	net.addLink(h3 , s2)
	net.addLink(h4 , s2)
	net.addLink(s1 , s2, bw=10, delay='200ms', loss=0)
	net.start()
	CLI(net)
	net.stop()


setLogLevel('info')
build_network()


