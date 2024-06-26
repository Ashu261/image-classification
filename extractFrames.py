import os
import cv2

# Define your dataset path
dataset_path = r"C:\Users\HP\Downloads\DAiSEE\DataSet"

# Example function to extract frames
def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_folder, f"frame_{count:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        count += 1
    cap.release()

# Iterate through the dataset and extract frames
for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.endswith((".avi", ".mp4")):
            video_path = os.path.join(root, file)
            output_folder = root  # You can change this to a different folder if needed
            extract_frames(video_path, output_folder)
