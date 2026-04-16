SDN Project using Mininet and POX Controller
📌 Project Title

Software Defined Networking (SDN) Simulation using Mininet and POX Controller

🎯 Project Description

This project demonstrates the working of a Software Defined Network (SDN) using:

Mininet → to create virtual network topology (hosts + switches)
POX Controller → to control the network behavior
OpenFlow Protocol → communication between switches and controller

The main objective is to implement a learning-based Layer 2 switch using SDN concepts, where the controller dynamically learns MAC addresses and installs flow rules in switches.

🧠 Key Concepts Used
SDN (Software Defined Networking)
OpenFlow 1.0 protocol
Packet-In and Flow-Mod messages
MAC learning (Layer 2 switching)
Event-driven controller programming
Network topology simulation using Mininet
🏗️ Project Architecture
        +----------------------+
        |   POX Controller     |
        |  (Control Plane)     |
        +----------+-----------+
                   |
        OpenFlow Protocol
                   |
  -----------------------------------
  |            |            |       |
 Switch s1   s2           s3   (Data Plane)
  |            |            |
 h1           h2           h3
⚙️ Working Flow
Hosts send data packets
Switch receives unknown packets
Switch forwards Packet-In to controller
Controller:
Learns source MAC address
Determines output port
Installs flow rule in switch
Switch forwards future packets directly without controller
📂 Project Files
1. controller_pox.py

Custom POX controller that:

Handles switch connection/disconnection
Learns MAC addresses
Implements learning switch logic
Installs flow rules using OpenFlow messages
2. topology.py

Core POX topology module (framework file):

Maintains network entities (hosts, switches, links)
Handles events like Join/Leave
Tracks network state inside controller
🚀 How to Run the Project
🟢 Step 1: Start POX Controller
cd ~/pox
./pox.py openflow.of_01 misc.controller_pox
🔵 Step 2: Start Mininet (New Terminal)
sudo mn --topo linear,3 --controller=remote
🟡 Step 3: Inside Mininet CLI
Check connectivity:
pingall
Test link failure:
link s1 s2 down
pingall
Restore link:
link s1 s2 up
pingall
Exit Mininet:
exit
🔴 Step 4: Stop Controller

In POX terminal:

Ctrl + C
📊 Expected Output
Switches connect to controller successfully
MAC addresses are learned dynamically
Packets are forwarded efficiently
Network adapts to link failure and recovery
Full connectivity is restored after link repair
🔥 Features Implemented
✔ Learning switch behavior
✔ Dynamic flow rule installation
✔ Real-time packet handling
✔ Controller-switch communication
✔ Link failure testing using Mininet
⚠️ Requirements
Linux (Ubuntu recommended / VirtualBox supported)
Python 3.6 – 3.9 (recommended for POX)
Mininet
POX Controller
📌 Conclusion

This project demonstrates how SDN separates the control plane (POX controller) from the data plane (switches), enabling centralized network control, dynamic flow management, and intelligent packet forwarding.
