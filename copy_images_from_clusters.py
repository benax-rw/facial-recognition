import os
import shutil

def copy_images_from_clusters(cluster_folder, dataset_folder):
    # Get list of cluster folders
    cluster_folders = [folder for folder in os.listdir(cluster_folder) if os.path.isdir(os.path.join(cluster_folder, folder))]

    # Iterate through each cluster folder
    for cluster_name in cluster_folders:
        cluster_path = os.path.join(cluster_folder, cluster_name)
        # Get list of image files in the cluster folder
        image_files = [os.path.join(cluster_path, img) for img in os.listdir(cluster_path) if img.endswith('.jpg')]
        
        # Copy each image to the dataset folder
        for img_file in image_files:
            shutil.copy(img_file, dataset_folder)
            print(f"Copying {img_file} to {dataset_folder}")

    # Remove the 'dataset-clusters' folder after copying images
    shutil.rmtree(cluster_folder)
    print(f"Removed {cluster_folder} after copying images.")

if __name__ == "__main__":
    # Folder paths
    cluster_folder = "dataset-clusters"  # Folder containing cluster folders
    dataset_folder = "dataset"  # Destination folder to copy images
    
    # Call function to copy images from cluster folders back to dataset folder
    copy_images_from_clusters(cluster_folder, dataset_folder)
