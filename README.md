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


## Engineering Problems Explored

- Communicating with stateful blockchain nodes from stateless containers
- Handling credentials and configuration across environments
- Designing deployable services for Kubernetes rather than localhost execution
- Modeling production-style service boundaries
- Integrating external networks into cloud-native architectures


## Architecture Overview

The service acts as a bridge between cloud-native workloads and an external blockchain network.

It runs inside Kubernetes while communicating with independent systems that exist outside the cluster’s lifecycle (Bitcoin & Lightning nodes).

This models a real infrastructure scenario: stateless services coordinating with persistent distributed networks.


                 ┌────────────────────────────┐
                 │        Client / User       │
                 └─────────────┬──────────────┘
                               │ HTTP API
                               ▼
                ┌─────────────────────────────────┐
                │   FastAPI Service (Container)   │
                │  Stateless Kubernetes Workload  │
                └─────────────┬───────────────────┘
                              │
                              │ Service Networking
                              ▼
        ┌──────────────────────────────────────────────┐
        │               Kubernetes Cluster              │
        │  - Pod Scheduling                             │
        │  - Secrets / ConfigMaps                       │
        │  - Helm Deployment                            │
        └─────────────┬──────────────┬────────────────┘
                      │              │
                      │              │
                      ▼              ▼
        ┌──────────────────┐   ┌──────────────────────┐
        │  Bitcoin Node    │   │     AWS Services     │
        │ (Persistent Net) │   │  (S3 / IAM / APIs)   │
        └──────────────────┘   └──────────────────────┘
                      │
                      ▼
            ┌────────────────────┐
            │ Lightning Network  │
            │   Future Layer     │
            └────────────────────┘
