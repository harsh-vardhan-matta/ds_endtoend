import os  # Importing the OS module for file and directory operations
from pathlib import Path  # Importing Path from pathlib for handling file paths
import logging  # Importing logging for debugging and status messages

# Configure logging to display INFO level messages
logging.basicConfig(level=logging.INFO)

# Define the project name
project_name = "mlproject"

# List of file paths to be created within the project
list_of_files = [
    f"D:\\Datasets\\ml_end_to_end\\src\\{project_name}\\__init__.py",
    f"D:\\Datasets\\ml_end_to_end\\src\\{project_name}\\components\\__init__.py",
    f"D:\\Datasets\\ml_end_to_end\\src\\{project_name}\\components\\data_ingestion.py",
    f"D:\\Datasets\\ml_end_to_end\\src\\{project_name}\\components\\data_transformation.py",
    f"D:\\Datasets\\ml_end_to_end\\src\\{project_name}\\components\\data_trainer.py",
    f"D:\\Datasets\\ml_end_to_end\\src\\{project_name}\\components\\data_monitoring.py",
    f"D:\\Datasets\\ml_end_to_end\\src\\{project_name}\\pipelines\\__init__.py",
    f"D:\\Datasets\\ml_end_to_end\\src\\{project_name}\\pipelines\\training_pipelines.py",
    f"D:\\Datasets\\ml_end_to_end\\src\\{project_name}\\pipelines\\prediction_pipelines.py",
    f"D:\\Datasets\\ml_end_to_end\\src\\{project_name}\\expection.py",
    f"D:\\Datasets\\ml_end_to_end\\src\\{project_name}\\logger.py",
    f"D:\\Datasets\\ml_end_to_end\\src\\{project_name}\\utils.py",
    "main.py",
    "app.py", 
    "requirements.txt",
    "setup.py"
]


# Iterate over the list of file paths
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string file path to a Path object
    filedir, filename = os.path.split(filepath)  # Split file path into directory and filename

    if filedir != "":  # Ensure the directory path is not empty
        os.makedirs(filedir, exist_ok=True)  # Create directory if it doesn’t exist
        logging.info(f"Creating directory: {filedir} for the file {filename}")  # Log directory creation

    # Check if the file does not exist OR is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  
        with open(filepath, 'w') as f:  # Open the file in write mode (creates an empty file)
            pass  # No content is written, just ensures the file exists
        logging.info(f"Creating empty file: {filepath}")  # Log file creation

    else:
        logging.info(f"{filename} already exists")  # Log if the file already exists and has content
