import cv2
import os
import platform
import sys

def display_images_in_folder(folder_path):
    # Get list of image files
    image_files = [os.path.join(folder_path, img) for img in os.listdir(folder_path) if img.endswith('.jpg')]
    
    # Sort the files for consistency
    image_files.sort()
    
    for img_file in image_files:
        img = cv2.imread(img_file)
        if img is None:
            print(f"Error loading image: {img_file}")
            continue
        
        # Resize the image to double resolution
        img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        
        # Get screen resolution
        screen_width, screen_height = get_screen_resolution()
        
        # Calculate window position
        window_width = img.shape[1]
        window_height = img.shape[0]
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Create a window and display the image
        cv2.namedWindow('Cluster Images', cv2.WINDOW_NORMAL)
        cv2.moveWindow('Cluster Images', x_position, y_position)
        cv2.imshow('Cluster Images', img)
        cv2.waitKey(250)  # Display for 1 second
        cv2.destroyAllWindows()

def get_screen_resolution():
    # Get screen resolution based on platform
    screen_width = 0
    screen_height = 0
    if platform.system() == "Windows":
        import ctypes
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
    elif platform.system() == "Darwin":  # macOS
        screen_width = 1280  # default value if unable to get actual screen resolution
        screen_height = 720  # default value if unable to get actual screen resolution
    elif platform.system() == "Linux":
        import subprocess
        try:
            output = subprocess.check_output(["xrandr"]).decode("utf-8")
            for line in output.splitlines():
                if " connected" in line:
                    resolution = line.split()[2]
                    screen_width, screen_height = map(int, resolution.split("x"))
                    break
        except (subprocess.CalledProcessError, IndexError, ValueError):
            pass
    return screen_width, screen_height

if __name__ == "__main__":
    # Get folder name 
    folder_name = "dataset"
    folder_path = os.path.join(folder_name)

    # Call the function to display images in the folder
    display_images_in_folder(folder_path)
