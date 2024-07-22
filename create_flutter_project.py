import os
import subprocess
import sys

# Define the project name and bundle ID
project_name = input("Enter Project Name eg: 'project_name' : ")
bundle_id = input("Enter Project Bundle ID eg: 'com.ujjval.project' : ")

# Define the predefined project structure
project_structure = [
    "lib/screens",
    "lib/models",
    "lib/controllers",
    "lib/utils",
]

project_files = [
    'lib/utils/colors.dart',
    'lib/utils/keys.dart',
    'lib/utils/tools.dart',
    'lib/utils/styles.dart',
]
# Define the dependencies to add
dependencies = [
    "http",
    "google_fonts",
    "firebase_core",
    "firebase_auth",
    "cloud_firestore",
    "cached_network_image",
    "firebase_crashlytics",
    "firebase_analytics",
    "logger",
    "flutter_screenutil",
    "fluttertoast"
]

# Function to run a command and capture output
def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout

# Step 1: Create a new Flutter project
print(f"Creating new Flutter project... with {bundle_id} and {project_name}")
run_command(f"flutter create --org {bundle_id} {project_name}")

# Change to project directory
os.chdir(project_name)

# Step 2: Create the predefined project structure
print("Creating project structure...")
for folder in project_structure:
    os.makedirs(folder, exist_ok=True)

# Step 3: Create predefined files
for file in project_files:
    open(file,'w')

# Step 4: Add predefined dependencies using flutter pub add
print("Adding dependencies to the project...")
dep = ''

for dependency in dependencies:
    dep += dependency + " "
run_command(f"flutter pub add {dep}")    

# Step 5: Get the dependencies
print("Getting Flutter dependencies...")
run_command("flutter pub get")

print("Flutter project setup complete.")
