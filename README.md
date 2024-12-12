# MQTT


## Description
This project uses the MQTT protocol to implement a publisher and subscriber architecture. Docker containers are used to run two applications: a publisher and a subscriber, which communicate through an MQTT broker.

## Project Links
- **Docker Hub Repository**: [estebanandres/mqtt-pub on Docker Hub](https://hub.docker.com/repository/docker/estebanandres/rest-api/general)
[estebanandres/mqtt-sub on Docker Hub](https://hub.docker.com/repository/docker/estebanandres/rest-api/general)

## Getting Started

### Cloning the Repository
To clone the repository, use the following command:
```bash
git clone https://github.com/EstebanASM/MQTT.git
```
Navigate to the project directory:
```bash
cd MQTT
```

### Running the Application Locally (Without Docker)
#### Prerequisites
- Ensure[Node.js](https://www.python.org/downloads/) is installed on your machine.

- Install the paho-mqtt library by running:
   ```bash
   pip install paho-mqtt

   ```

#### Running the Publisher
1. Open a terminal and run:
   ```bash
   python MqttPub.py

   ```
2. The publisher will send messages to the topic test/topic every 2 seconds.

#### Running the Subscriber
1. In another terminal, run:
   ```bash
   python MqttSub.py

   ```
2. The subscriber will display the messages received from the topic test/topic.


### Running the Application with Docker

To run the application with Docker, visit the Docker Hub repository for this project: [estebanandres/mqtt-pub on Docker Hub](https://hub.docker.com/repository/docker/estebanandres/rest-api/general)
[estebanandres/mqtt-sub on Docker Hub](https://hub.docker.com/repository/docker/estebanandres/rest-api/general)