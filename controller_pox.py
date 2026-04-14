from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

mac_to_port = {}

def _handle_PacketIn(event):
    packet = event.parsed

    # Safety check
    if not packet.parsed:
        return

    # Allow only ARP and IP packets
    if packet.type not in (0x0800, 0x0806):
        return

    dpid = event.connection.dpid
    mac_to_port.setdefault(dpid, {})

    src = packet.src
    dst = packet.dst

    # Learn MAC address
    mac_to_port[dpid][src] = event.port

    if dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][dst]
    else:
        out_port = of.OFPP_FLOOD

    actions = [of.ofp_action_output(port=out_port)]

    # Install flow rule
    if out_port != of.OFPP_FLOOD:
        match = of.ofp_match()
        match.dl_dst = dst

        msg = of.ofp_flow_mod()
        msg.match = match
        msg.actions = actions
        event.connection.send(msg)

    # Send packet
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions = actions
    msg.in_port = event.port
    event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("POX Controller Running...")
