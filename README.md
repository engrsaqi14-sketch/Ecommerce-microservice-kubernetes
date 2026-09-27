<<<<<<< HEAD
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
=======
This is a Ecommerce microservice architectural deployed using Kubernetes: 

ecommerce-k8s/
│
├── frontend/
│
├── services/
│   ├── product-service/
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   └── venv/
│   │
│   └── order-service/
│       ├── main.py
│       ├── requirements.txt
│       ├── Dockerfile
│       └── venv/
│
└── k8s/
    ├── namespace.yaml
    ├── product-deployment.yaml
    └── product-service.yaml
>>>>>>> 5a106b2 (updates)
