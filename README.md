This is a Ecommerce deployed using Kubernetes: 
                    Kubernetes
                        │
                     Ingress
                        │
                    Frontend
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
       Product Service        Order Service
             │                     │
             ▼                     ▼
           Redis               PostgreSQL
                                  │
                                 PVC
