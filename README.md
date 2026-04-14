# SDN Mininet Project

## Topic
Link Failure Detection and Recovery using SDN

## Description
In this project, I have implemented a simple SDN network using Mininet and POX controller. The main aim is to understand how the controller communicates with switches and how flow rules are installed.

The controller used here is POX with a learning switch logic. It handles packet_in events and installs flow rules based on MAC addresses.

---

## Topology
The network consists of:
- 2 hosts (h1, h2)
- 3 switches (s1, s2, s3)

The switches are connected in such a way that there is an alternate path available. This helps in testing link failure and recovery.

---

## How to Run

### Step 1: Start controller
cd ~/pox  
./pox.py forwarding.l2_learning  

### Step 2: Run topology
sudo mn -c  
sudo python3 topology.py  

---

## Testing

### 1. Normal case
mininet> pingall  

Screenshot 1: ping working successfully  

---

### 2. Link failure
mininet> link s1 s2 down  
mininet> pingall  

Screenshot 2: packets are dropped  

---

### 3. Link recovery
mininet> link s1 s2 up  
mininet> pingall  

Screenshot 3: communication restored  

---

## Performance

### Ping
mininet> h1 ping h2  

Screenshot 4: ping output  

### Throughput
mininet> iperf h1 h2  

Screenshot 5: iperf result  

### Flow table
sudo ovs-ofctl dump-flows s1  

Screenshot 6: flow table entries  

---

## Output
- Hosts are able to communicate in normal condition  
- When link is down, communication fails  
- After link is restored, communication works again  
- Flow rules are installed dynamically  

---

## Conclusion
This project helped me understand how SDN works. The controller controls the network and updates flow rules based on traffic. It also shows how network reacts during link failure and recovery.

---
