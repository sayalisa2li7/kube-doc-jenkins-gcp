# kube-doc-jenkins-gcp

**Setting up the GCP environment**:

- Created a Google Cloud Platform account.
- Set up a project in the Google Cloud Console.
- Enable the Kubernetes Engine API and Container Registry API.

**Created a service account with necessary permissions and files**

- gcloud iam service-accounts create sayalisa2li7 --description="gcr-service-acc"
- gcloud iam service-accounts list
- gcloud projects add-iam-policy-binding kube-doc-jenkins     --member="serviceAccount:sayalisa2li7@kube-doc-jenkins.iam.gserviceaccount.com"     --role="roles/artifactregistry.writer"
- gcloud projects get-iam-policy kube-doc-jenkins
- gcloud iam service-accounts keys create ./service-account-key.json <--iam-account=sayalisa2li7@kube-doc-jenkins.iam.gserviceaccount.com>

**Containerize the web application**:

- Dockerized the web application by writing a Dockerfile. This file describes the steps needed to create a Docker image for the application.
- Built and pushed the Docker image to Google Container Registry (GCR).

- sudo docker login -u \_json\_key --password-stdin https://gcr.io < ./service-account-key.json
- Gave artifactregistry.repositories.createOnPush permission using GCP console.
- sudo docker push gcr.io/kube-doc-jenkins/fibonacci-app:1.0

**Run the image to check if it is working properly**

- sudo docker run -p 8082:8080 gcr.io/kube-doc-jenkins/fibonacci-app:1.0

**Set up Kubernetes cluster**:

- Use Google Kubernetes Engine (GKE) to create a Kubernetes cluster where the application will be deployed.
- gcloud container clusters create gcp-cluster --zone us-central1-a --num-nodes 1
- Configure kubectl, the Kubernetes command-line tool, to interact with the GKE cluster.

- curl -LO "https://dl.k8s.io/release/$(curl -L -s <https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl>"
- chmod +x kubectl
- sudo mv kubectl /usr/local/bin/
- kubectl version –client
- kubectl cluster-info
- sudo apt-get install google-cloud-sdk-gke-gcloud-auth-plugin
- gke-gcloud-auth-plugin –version
- gcloud container clusters get-credentials gcp-cluster --zone us-central1-a
- kubectl cluster-info

**Command to delete the clusters:**

- gcloud container clusters delete gcp-cluster --zone us-central1-a

**Deploy the application using Kubernetes**:

- Wrote Kubernetes manifests (YAML files) to define the application's deployment, service, and other resources.
- Applied these manifests to the Kubernetes cluster to deploy the application.

**Set up Jenkins**:

- Install Jenkins on a virtual machine or a container in the GCP environment.
- Configure Jenkins with necessary plugins for Docker, Kubernetes.

**Set up Jenkins pipeline**:

- Create a Jenkins pipeline script (Jenkinsfile) that defines the CI/CD process.
- The pipeline script includes stages for building the Docker image, pushing it to the container registry, and deploying it to the Kubernetes cluster.

**Configure Jenkins credentials**:

- Add credentials to Jenkins to authenticate with the Docker registry and Kubernetes cluster.
