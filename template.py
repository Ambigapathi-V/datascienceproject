import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Datascience'

# List of files to create
list_of_files = [
    'github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",  # Added a slash
    f"src/{project_name}/utils/common.py",    # Added a slash
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    'config/config.yaml',
    "params.yaml",
    "schema.py",
    'main.py',
    "Dockerfile",
    "setup.py",  # Corrected from "setp.py"
    "research/research.ipynb",
    "templates/index.html"
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory {filedir} for the file: {filename}")

    # Create an empty file if it doesn't exist or if it's empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            f.write("# Empty file\n")
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
