Face Recognition Project
***************
Created by Gabriel Baziramwabo
Founder of Benax Technologies Ltd.
***************
1. File System:
The "tree" command typically returns the following file system:
- ├── copy_images_from_clusters.py
- ├── create_clusters.py
- ├── create_dataset.py
- ├── dataset
- │   ├── data.1.1711973742082.jpg
- │   ├── data.1.1711973742672.jpg
- │   ├── data...............
- ├── models
- │   ├── haarcascade_frontalface_default.xml
- │   └── trained_lbph_face_recognizer_model.yml
- ├── predict.py
- ├── predict_and_control.py
- ├── review_cluster.py
- ├── review_dataset.py
- └── train_model.py

2. Environment Configuration:<br>
2.1. Programming Language
   Python3.10 or plus
2.2. Libraries<br>
2.2.1. General AI Project Libraries:
   - os: Operating system interface, for file and directory operations.
   - shutil: High-level file operations, for copying and removing files.
   - numpy: For numerical operations and array manipulation.
   - tensorflow: Deep learning library for building and training neural networks.
   - tensorflow.keras: High-level neural networks API for TensorFlow.
   - sklearn: For machine learning algorithms and utilities.
   - cv2 or opencv-python: OpenCV library for computer vision tasks.
   - time: For time-related operations and delays.
   - serial: For serial communication with devices (e.g., Arduino).

2.2.2. Specific to Face Recognition and Detection:
   - tensorflow.keras.applications: Pre-trained models for image classification tasks (e.g., VGG16).
   - tensorflow.keras.preprocessing.image: For image preprocessing tasks.
   - sklearn.cluster.KMeans: For K-means clustering.
   - tqdm: For progress bars and monitoring loops.
   - PIL (Python Imaging Library): For image processing and manipulation (e.g., converting to grayscale).

3. Procedure:
- 3.1. Create Dataset: "python create_dataset.py". Before recording a face give it an ID.
- 3.2. Review Dataset: "python review_dataset.py". This displays images located in the "dataset" directory one after another.
- 3.3. Create Clusters: "python create_clusters.py". The "dataset" directory is emptied after the clusters are created.
- 3.4. Review Cluster: "python review_cluster.py Clusterk" where k=1,2,3,...n clusters
- 3.5. Manually delete the cluster containing fake faces.
- 3.6. Copy faces from remaining clusters: "python copy_images_from_clusters.py". This returns the images from clusters and then the cluster folders are destroyed. 
- 3.7. Train the model "LBPH Face Recognizer": "python train_model.py". trained_lbph_face_recognizer_model.yml is the file where the trained LBPH Face Recognizer model is serialized and saved. It can be loaded later to perform face recognition on new images without the need to retrain the model every time.
- 3.8. Edit the file "predict.py" to give the person name to the face ID.
- 3.9. Make prediction on the new unseen faces: "python predict.py"
- 3.10. Based on the prediction made, control a device connected to the PC on which this AI progragram is running: "python predict_and_control.py". Look for the file sample_arduino_program.ino" which receives data from the host PC and control an LED accordingly.
