# 🚀 Python Flask DevOps Project on AWS EKS (End-to-End)

This is a complete **hands-on DevOps project** built using real-world DevOps tools and cloud deployment practices.

✅ Flask Web App  
✅ Docker Containerization  
✅ Git & GitHub Version Control  
✅ AWS ECR (Container Registry)  
✅ AWS EKS (Kubernetes Cluster)  
✅ Jenkins CI/CD Pipeline  
✅ Kubernetes Deployment + LoadBalancer Service  

---

## 👨‍💻 Author
**Sharana Basava (DevOps Engineer)**

---

## 🧰 Tools & Technologies Used

### ✅ Programming / App
- **Python**
- **Flask**

### ✅ OS / CLI
- **Linux**
- **Git Bash (Windows)**

### ✅ Version Control
- **Git**
- **GitHub**

### ✅ Containerization
- **Docker**
- **AWS ECR**

### ✅ CI/CD
- **Jenkins Pipeline**

### ✅ Orchestration
- **Kubernetes**
- **AWS EKS**

### ✅ IaC & Config Management (Planned / Next)
- **Terraform**
- **Ansible**

### ✅ Monitoring (Planned / Next)
- **Prometheus**
- **Grafana**

---

# 📁 Project Structure
python-flask-devops-eks/
│
├── app/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
│
├── jenkins/
│ └── Jenkinsfile
│
├── terraform/ # (Phase 6 - Next)
├── ansible/ # (Phase 7 - Next)
└── README.md

✅ PHASE 2: Dockerize the Flask App
1️⃣ Build Docker Image
docker build -t flask-devops ./app

2️⃣ Run Docker container
docker run -p 5000:5000 flask-devops


✅ Output:

App available at: http://localhost:5000

✅ PHASE 3: Push Docker Image to AWS ECR
1️⃣ Login to AWS ECR
aws ecr get-login-password --region ap-south-1 \
| docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com

2️⃣ Tag image
docker tag flask-devops:latest <ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/flask-devops:latest

3️⃣ Push image
docker push <ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/flask-devops:latest

✅ PHASE 4: Deploy Application to AWS EKS (Kubernetes)
1️⃣ Create EKS cluster
eksctl create cluster \
--name devops-eks-cluster \
--region ap-south-1 \
--nodegroup-name devops-nodes \
--node-type t3.medium \
--nodes 2 \
--managed

2️⃣ Verify nodes
kubectl get nodes


✅ Nodes should be Ready

3️⃣ Deploy Kubernetes manifests
kubectl apply -f k8s/

4️⃣ Get LoadBalancer URL
kubectl get svc


✅ Output includes External LoadBalancer URL like:

http://xxxxxxxx.ap-south-1.elb.amazonaws.com

✅ PHASE 5: Jenkins CI/CD Pipeline
✅ Goal

Automate:
✅ GitHub → Jenkins → Docker Build → ECR Push → EKS Deploy

1️⃣ Jenkins installed on AWS EC2

Jenkins runs on port 8080

Docker installed

AWS CLI installed

kubectl installed

kubeconfig connected to EKS

2️⃣ Jenkins Credentials

AWS credentials stored in Jenkins as:

Credential ID: aws-creds

3️⃣ Jenkinsfile Pipeline

Pipeline stages:

Docker build

ECR login

Push Docker image to ECR

Deploy to EKS using kubectl

4️⃣ Build Trigger

Manual build done using Build Now in Jenkins.

✅ Output (Final Result)

✅ Flask app is live on AWS EKS
✅ Public endpoint is accessible through AWS LoadBalancer
✅ Jenkins automates the deployment pipeline
