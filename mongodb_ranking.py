#-----------------------------------------------------------------------------------------
"""
Load the Libraries
"""

from bson import decode_file_iter
from bson import ObjectId
from collections import Counter
from urllib.parse import urlparse

# Function to extract project name from a GitHub URL
def extract_project_name(url):
    path_parts = urlparse(url).path.split('/')
    if len(path_parts) >= 5:
        return path_parts[3]
    return None

def get_project_name_by_pull_request_system_id(pull_request_system_id, ll, mm):
    for ll_item in ll:
        if ll_item['pull_request_system_id'] == pull_request_system_id:
            for mm_item in mm:
                if mm_item['_id'] == ll_item['pull_request_system_id']:
                    project_name = extract_project_name(mm_item['url'])
                    if project_name:
                        return project_name
    return None

# Path to your BSON file
bson_file_identity = 'final_identity.bson'
bson_file_people = 'people.bson'
bson_file_pull_request = 'pull_request.bson'
bson_file_pull_request_system = 'pull_request_system.bson'

# Initialize an empty list to store decoded documents
final_decoded_documents = []
decoded_documents = []
pull_request_documents = []
pull_request_system_documents = []

# Open the BSON file and decode each document
with open(bson_file_identity, 'rb') as bson_file:
    for document in decode_file_iter(bson_file):
        final_decoded_documents.append(document)

with open(bson_file_people, 'rb') as bson_file:
    for document in decode_file_iter(bson_file):
        decoded_documents.append(document)

with open(bson_file_pull_request, 'rb') as bson_file:
    for document in decode_file_iter(bson_file):
        pull_request_documents.append(document)

with open(bson_file_pull_request_system, 'rb') as bson_file:
    for document in decode_file_iter(bson_file):
        pull_request_system_documents.append(document)

def get_people_ids(data, _id):
    for item in data:
        if item['_id'] == ObjectId(_id):
            return item['people']
    return []

def find_by_id_people(data, object_id):
    for item in data:
        if item['_id'] == ObjectId(object_id):
            return {'name': item['name'], 'email': item['email']}
    return None

# Debug: Print number of documents retrieved from BSON files
print(f"Number of pull requests retrieved: {len(pull_request_documents)}")
print(f"Number of pull request systems retrieved: {len(pull_request_system_documents)}")

# Function to rank developers for a given project
def rank_developers_for_project(project_name, project_ll, decoded_documents):
    developer_details = []
    for event in project_ll:
        _id = ObjectId(event['creator_id'])
        result = find_by_id_people(decoded_documents, _id)
        if result:
            name_email = (result['name'], result['email'])
            developer_details.append(name_email)

    # Count the most repeated pull request
    counter = Counter(developer_details)
    most_common_10 = counter.most_common(20)

    # Print the top 20 most common developer details
    print(f"Project: {project_name}")
    for idx, (name_email, count) in enumerate(most_common_10, start=1):
        print(f"Rank {idx}. Developer Name: {name_email[0]}, Email: {name_email[1]}")

# Track processed projects
processed_projects = set()

# Loop through the projects and process each unique project
for pull_request in pull_request_documents:
    pull_request_system_id = pull_request['pull_request_system_id']

    # Get the project name for the current pull request system ID
    project_name = get_project_name_by_pull_request_system_id(pull_request_system_id, pull_request_documents, pull_request_system_documents)

    # Check if the project has already been processed
    if project_name and project_name not in processed_projects:
        # Mark the project as processed
        processed_projects.add(project_name)

        # Filter pull requests for the current project
        project_ll = [pr for pr in pull_request_documents if pr['pull_request_system_id'] == pull_request_system_id]

        # Rank developers for the current project
        rank_developers_for_project(project_name, project_ll, decoded_documents)

        # Stop after processing 5 projects
        if len(processed_projects) >= 5:
            break
