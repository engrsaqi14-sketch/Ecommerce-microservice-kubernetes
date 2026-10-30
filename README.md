# E-Commerce Microservices on Kubernetes

A hands-on DevOps project demonstrating containerization, Kubernetes orchestration, and automated CI/CD.

## Tech Stack

- Docker and Kubernetes (Minikube)
- GitHub Actions and GitHub Container Registry (GHCR)
- Product and Order microservices
- Redis and PostgreSQL
- Kubernetes Services, Ingress, health probes, and resource limits

## Architecture

```text
Developer → GitHub Actions → Docker Build
                  ↓
                 GHCR
                  ↓
          Self-hosted Runner
                  ↓
               Minikube
                  ↓
       Product & Order Services
             ↓          ↓
           Redis    PostgreSQL
```

## CI/CD Pipeline

The workflow in `.github/workflows/ci.yml`:

1. Builds Docker images for Product and Order services.
2. Pushes images to GHCR.
3. Deploys updated images to Minikube through a self-hosted runner.
4. Verifies Kubernetes rollout status.

## Run and Verify

```bash
kubectl get pods -n ecommerce
kubectl get services -n ecommerce
kubectl get deployments -n ecommerce
```

## Key Learning Outcomes

- Docker image builds and registry publishing
- Kubernetes deployments, services, and resource management
- Automated CI/CD and rolling deployments
- Health checks and deployment troubleshooting

## Repository

[View the project on GitHub](https://github.com/engrsaqi14-sketch/Ecommerce-microservice-kubernetes)
