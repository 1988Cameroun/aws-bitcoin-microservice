## Purpose

This project explores a real infrastructure challenge: enabling cloud-native applications to safely interact with long-running external networks such as Bitcoin nodes.

Instead of being a typical REST microservice, the system models production concerns including container orchestration, service isolation, secrets handling, and reliable communication between stateless workloads and persistent blockchain processes.

The goal is to demonstrate platform-level thinking — how applications behave when they leave localhost and must coordinate with independent networks.


## What This Project Demonstrates

- Integrating Kubernetes services with external stateful infrastructure
- Managing communication with blockchain nodes from ephemeral containers
- Designing deployable infrastructure rather than local development scripts
- Modeling real-world operational boundaries
- Preparing services for Lightning Network expansion
