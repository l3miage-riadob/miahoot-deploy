import os
from google.oauth2 import service_account
from google.cloud import container_v1
from kubernetes import client, config
from kubernetes.client.rest import ApiException

# Path to the service account key JSON file
key_path = "path/to/your/key.json"

# Set the environment variable for the service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

# Create credentials object from the service account key
credentials = service_account.Credentials.from_service_account_file(key_path)

# Set the default project ID
project_id = "your-project-id"
container_client = container_v1.ClusterManagerClient(credentials=credentials)
container_client.project_id = project_id

# Set the default zone
zone = "us-central1-a"


# Path to the directory containing the Kompose-generated YAML files
yaml_dir = "path/to/your/yaml/files"

# Namespace for the Kubernetes resources
namespace = "your-namespace"

# Load the Kubernetes configuration from the default location
config.load_kube_config()

# Create a Kubernetes API client object
api_client = client.ApiClient()

# Create the Kubernetes objects from the YAML files
k8s_objects = []
for filename in os.listdir(yaml_dir):
    with open(os.path.join(yaml_dir, filename)) as f:
        k8s_objects.extend(list(client.V1ObjectSerializer().deserialize(f.read())))

# Deploy the Kubernetes objects to the cluster
api_instance = client.CoreV1Api(api_client)
for obj in k8s_objects:
    try:
        api_response = api_instance.create_namespaced_object(body=obj, namespace=namespace)
        print(f"Created {obj.kind} {obj.metadata.name} in namespace {namespace}")
    except ApiException as e:
        print(f"Exception when creating object: {e}\n")
