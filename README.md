# SDN Project using Mininet and POX Controller

## Project Title
Software Defined Networking (SDN) Simulation using Mininet and POX Controller

---

## Project Description

This project demonstrates Software Defined Networking (SDN) using Mininet and the POX controller.

Mininet is used to create a virtual network topology with hosts and switches, while the POX controller manages the network behavior using the OpenFlow protocol.

The controller acts as the brain of the network and implements a learning switch. It learns MAC addresses dynamically and installs flow rules in switches to optimize packet forwarding.

---

## Technologies Used

- Mininet (Network Emulator)
- POX Controller
- OpenFlow Protocol
- Python

---

## Topology Used

Linear topology with 3 switches and 3 hosts:

h1 --- s1 --- s2 --- s3 --- h3  
          |  
         h2  

---

## Working Principle

1. Hosts send packets through switches.
2. Switch sends unknown packets to controller (Packet-In event).
3. Controller learns source MAC address.
4. Controller checks destination MAC address:
   - If known → sends directly
   - If unknown → floods packet
5. Controller installs flow rules in switches.
6. Future packets are forwarded directly by switches.

---

## Files in Project

### controller_pox.py
Custom POX controller that:
- Handles switch connection and disconnection
- Learns MAC addresses dynamically
- Processes Packet-In events
- Installs flow rules in switches

---

### topology.py
POX topology module that:
- Maintains network entities (hosts, switches)
- Handles network events
- Tracks topology state inside controller

---

## How to Run

### Step 1: Start POX Controller
cd ~/pox
./pox.py openflow.of_01 misc.controller_pox

---

### Step 2: Start Mininet (new terminal)
sudo mn --topo linear,3 --controller=remote

---

### Step 3: Inside Mininet CLI

pingall

link s1 s2 down
pingall

link s1 s2 up
pingall

exit

---

### Step 4: Stop Controller
Press Ctrl + C in POX terminal

---

## Expected Output

- Switches connect to controller successfully
- MAC learning happens dynamically
- Packets are forwarded correctly
- Link failure affects connectivity
- Network restores after link recovery

---

## Conclusion

This project demonstrates SDN principles where the controller centrally manages the network and switches act as simple forwarding devices. It shows dynamic MAC learning, flow rule installation, and real-time network control using OpenFlow.
