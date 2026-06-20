The system allows multiple publishers and subscribers to communicate asynchronously through topic-based message distribution.

<img width="1535" height="815" alt="task02" src="https://github.com/user-attachments/assets/3e942627-c7e5-407d-a61d-6ea87560c058" />

<img width="1536" height="813" alt="task03" src="https://github.com/user-attachments/assets/2dcc8ad4-ccdd-42a2-a349-0225c4faf7a3" />

To improve availability, the system extended into a multi-server failover architecture. Instead of relying on a single server, multiple server instances (brokers) are run on different ports. The client maintains a list of available servers and attempts to connect to the primary server. If the primary server fails, the client automatically reconnects to a backup server.

This approach reduces downtime and eliminates the single point of failure in the system. This is a simplified implementation to distributed messaging systems, it effectively failover handling and improved system availability. 

Run multiple servers;

python server.py 5000
python server.py 5001
python server.py 5002

python client.py PUBLISHER SPORTS
python client.py SUBSCRIBER SPORTS
python client.py SUBSCRIBER BLOG

When One server dies, clients reconnects automatically to a another server. The system will works without any interruption. 

This implementation improves availability, but not full message reliability, because brokers do not replicate messages to each other.
<img width="1536" height="816" alt="01" src="https://github.com/user-attachments/assets/23d05738-34a3-4163-847d-d0cd9ba23bb8" />

<img width="1536" height="816" alt="02" src="https://github.com/user-attachments/assets/069b5586-24b3-4e75-8638-4f401b4aacc4" />
