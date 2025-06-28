# Custom YOLO Object Detection Project

## Project Overview

In this project, you will create a custom object detection system using the YOLO (You Only Look Once) algorithm. You'll go through the entire machine learning pipeline, from data collection to model deployment in a real-time application.

## Project Steps

1. Data Collection and Annotation
2. Dataset Preparation
3. Model Training
4. Real-time Detection Implementation
5. Project Extensions

## 1. Data Collection and Annotation

### Task 1.1: Collect Images
- Gather at least 100 images of your chosen object(s)
- Ensure variety in angles, lighting, and backgrounds
- Use smartphone cameras or download images (ensure you have rights to use them)

### Task 1.2: Annotate Images
- Use LabelImg tool (https://github.com/tzutalin/labelImg)
- Install LabelImg: `pip install labelImg`
- Run LabelImg: `labelImg`
- Draw bounding boxes around your objects
- Save annotations in YOLO format

## 2. Dataset Preparation

### Task 2.1: Organize Your Dataset
Create the following directory structure:
```
custom_dataset/
    images/
        train/
        val/
    labels/
        train/
        val/
```

### Task 2.2: Split Your Dataset
- Place 80% of your images and their corresponding label files in the train folders
- Place the remaining 20% in the val folders

### Task 2.3: Create data.yaml
Create a file named `data.yaml` in your `custom_dataset` folder with the following content:
```yaml
train: custom_dataset/images/train
val: custom_dataset/images/val
nc: 1  # number of classes (change if you have more)
names: ['your_object_name']  # list of class names
```

## 3. Model Training

### Task 3.1: Set Up YOLOv5
```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

### Task 3.2: Start Training
Run the following command:
```bash
python train.py --img 640 --batch 16 --epochs 100 --data path/to/your/data.yaml --weights yolov5s.pt
```

### Task 3.3: Monitor Training
- Use Tensorboard to monitor training progress
- Run: `tensorboard --logdir runs/train`
- Open the provided URL in your browser

## 4. Real-time Detection Implementation

### Task 4.1: Create Detection Script
Create a new Python file named `realtime_detection.py` with the following content:

```python
import cv2
from ultralytics import YOLO
import numpy as np
import time

class CustomYOLODetection:
    def __init__(self, model_path='path/to/your/best.pt'):
        self.model = YOLO(model_path)
        self.cap = cv2.VideoCapture(0)
        self.class_names = self.model.names

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            results = self.model(frame)
            
            for result in results:
                boxes = result.boxes.cpu().numpy()
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0].astype(int)
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    label = f"{self.class_names[cls]} {conf:.2f}"
                    
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            cv2.imshow('Custom YOLO Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

detector = CustomYOLODetection('path/to/your/best.pt')
detector.run()
```

### Task 4.2: Run Real-time Detection
- Replace 'path/to/your/best.pt' with the actual path to your trained model
- Run the script: `python realtime_detection.py`

## 5. Project Extensions

Choose one or more of these extensions to enhance your project:

### Extension 5.1: Multi-class Detection
- Collect and annotate images for multiple classes
- Update your `data.yaml` file accordingly
- Retrain your model and update the detection script

### Extension 5.2: Performance Optimization
- Experiment with different YOLO model sizes (e.g., YOLOv5m, YOLOv5l)
- Try different image sizes and batch sizes during training
- Implement inference optimizations (e.g., using ONNX runtime)

### Extension 5.3: Application Development
- Create a graphical user interface for your detection system
- Implement features like saving detected frames or counting objects
- Develop a specific use-case application (e.g., a security system that alerts when it detects a certain object)

### Extension 5.4: Deployment
- Deploy your model on a Raspberry Pi or other edge device
- Create a web application that uses your model for object detection on uploaded images

## Conclusion

By completing this project, you will have gained hands-on experience with the entire machine learning pipeline for object detection. You'll have developed skills in data preparation, model training, and application development, providing a strong foundation for further exploration in computer vision and deep learning.

Remember to document your process, challenges faced, and solutions found throughout the project. Good luck!
