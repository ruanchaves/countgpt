import os
import shutil
import pandas as pd
import argparse

def create_directory(path):
    """
    Create directory if it doesn't exist.
    
    Args:
        path (str): Directory path
    """
    if not os.path.exists(path):
        os.makedirs(path)


def read_csv(csv_file):
    """
    Read csv file and return unique ids from 'image_id' column.
    
    Args:
        csv_file (str): Path to csv file.
        
    Returns:
        list: Unique image ids.
    """
    df = pd.read_csv(csv_file)
    return df['image_id'].unique().tolist()


def copy_images(source_folder, destination_folder, ids):
    """
    Copy image files with specific ids from source_folder to destination_folder.
    
    Args:
        source_folder (str): Source directory path.
        destination_folder (str): Destination directory path.
        ids (list): List of image ids.
    """
    for id in ids:
        source_file = os.path.join(source_folder, f"v7w_{id}.jpg")
        if os.path.isfile(source_file):
            shutil.copy2(source_file, destination_folder)


def main():
    """
    Main function to execute the script.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Copy specific images from source directory to destination directory.')
    parser.add_argument('source_folder', type=str, help='Source directory path.')
    args = parser.parse_args()
    
    # Paths
    csv_file = 'data/v7w_telling/v7w_telling.csv'
    destination_folder = 'data/images'
    
    # Create directory if it doesn't exist
    create_directory(destination_folder)
    
    # Read csv file and get unique ids
    ids = read_csv(csv_file)
    
    # Copy images
    copy_images(args.source_folder, destination_folder, ids)


if __name__ == '__main__':
    main()
