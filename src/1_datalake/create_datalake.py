"""Create datalake in main directory"""

import os
import pkg_resources

STRUCTURE_FILE = 'datalake_structure.txt'

def get_datalake_dirs():
    """Returns datalake directories stored in the file structure.txt"""
    
    if not pkg_resources.resource_exists(__name__, STRUCTURE_FILE):
        raise FileNotFoundError(f"File {STRUCTURE_FILE} not found")
    
    with pkg_resources.resource_stream(__name__, STRUCTURE_FILE) as f:
        dirs = [dir.strip() for dir in f]  # Usar 'f' en lugar de 'dirs' aquí
    return dirs

def create_datalake(dirs):
    """Creates datalake in main directory"""
    
    for path in dirs:
        if not os.path.exists(path):
            os.makedirs(path)

def main():
    """Orquestar la creacion del datalake"""
    
    dirs = get_datalake_dirs()
    create_datalake(dirs)

if __name__ == "__main__":
    main()

    
