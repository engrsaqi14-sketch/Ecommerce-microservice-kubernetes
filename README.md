This is a Ecommerce deployed using Kubernetes: 
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
