# So-Semestral-Speedrun

## Description

This repository contains the source code and configurations for the semester project "so-semestral-speedrun". It demonstrates how to run containers with load balancing using NGINX reverse proxy.

## Getting Started

### Prerequisites

Before running the project, ensure that you have the following prerequisites:

- Linux Ubuntu Distro
- Docker and Docker Compose installed

### Running Containers

Follow these steps to run the containers:

1. Navigate to the `/containers` folder.
2. Run `docker-compose up` (or `docker compose up` for some Compose versions).
3. Observe the logs of the following containers by using the command: `docker logs -f <container-name>`:
   - Webnode1 
   - Webnode2
   - Nginx-reverse-proxy

### Testing Load Balancer

To test the load balancer, execute the `test_load_balancer.py` script:

```bash
python3 test_load_balancer.py
```

This script sends 100 requests and checks the response time of each request.

### Verification

After running the test, verify that the 100 requests have been load balanced by checking the logs between the `webnode1` and `webnode2` containers.

Enjoy the load balancing experience!
