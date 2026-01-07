from pathlib import Path
import logging
from typing import List


logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')


# Set your project name here
project_name: str = "SignLanguage"


# Files and templates to create for a new project
list_of_files: List[str] = [
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "template/index.html",
    ".dockerignore",
    "app.py",
]


def create_project_files(base_dir: str = ".") -> None:
    """Create directories and empty files listed in `list_of_files` under `base_dir`.

    Existing files are left untouched.
    """
    base = Path(base_dir)
    for relative_path in list_of_files:
        file_path = base / relative_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if not file_path.exists():
            file_path.touch()
            logging.info(f"Created: {file_path}")
        else:
            logging.info(f"Already exists: {file_path}")


if __name__ == "__main__":
    create_project_files()
