# Football Analysis Project

## Introduction
The goal of this project is to develop an advanced system to detect and track players, referees, and footballs in video footage using YOLO, one of the best AI object detection models available. This project not only includes training and improving the performance of the YOLO model but also incorporates a range of techniques to extract meaningful insights from football match videos.

### Objectives:
1. **Player and Referee Detection and Tracking**: Use YOLO to detect and track players, referees, and footballs in real-time video.
2. **Team Assignment**: Classify players into teams based on the colors of their t-shirts using K-means for pixel segmentation and clustering.
3. **Ball Acquisition Measurement**: Calculate the ball possession percentage for each team.
4. **Camera Movement Analysis**: Employ optical flow to measure camera movement between frames.
5. **Player Movement Measurement**: Implement perspective transformation to convert pixel movement to real-world distances (in meters).
6. **Performance Metrics**: Calculate speed and distance covered by players throughout the match.

This comprehensive approach addresses multiple real-world problems and provides a robust foundation for both beginners and experienced machine learning engineers interested in sports analytics.

![Screenshot](https://github.com/Devesh061102/13-Football-Analysis-Yolo/blob/main/output_videos/Screenshot%202024-07-13%20113226.png?raw=true)

## Modules Used
The project utilizes the following modules:

1. **YOLO (You Only Look Once)**:
   - **Purpose**: Object detection model.
   - **Application**: Detect and track players, referees, and footballs in video footage.
   - **Model Used**: Trained Yolov5x, further fine-tuned on a football player image dataset to identify the field, referees, and players.

2. **K-means Clustering**:
   - **Purpose**: Pixel segmentation and clustering.
   - **Application**: Detect t-shirt colors for team classification.

3. **Optical Flow**:
   - **Purpose**: Measure camera movement.
   - **Application**: Analyze the camera’s movement between frames to adjust player tracking data accordingly.

4. **Perspective Transformation**:
   - **Purpose**: Represent scene depth and perspective.
   - **Application**: Transform pixel measurements into real-world distances (meters), enhancing the accuracy of player movement analysis.

5. **Speed and Distance Calculation**:
   - **Purpose**: Quantify player performance.
   - **Application**: Calculate each player's speed and distance covered during the match.

## Detailed Workflow

### 1. Player and Referee Detection
- **YOLO Training**: 
  - Fine-tune the YOLOv5x model on a dataset specific to football player images.
  - Annotate training data to include players, referees, footballs, and the field.
  - Train the model to achieve high accuracy in detection.

### 2. Team Assignment
- **Color Segmentation**:
  - Use K-means clustering for segmenting the colors of the t-shirts worn by players.
  - Classify players into different teams based on dominant t-shirt colors.

### 3. Ball Acquisition Measurement
- **Possession Analysis**:
  - Track the football and determine which team has possession at any given time.
  - Calculate the percentage of time each team possesses the ball.

### 4. Camera Movement Analysis
- **Optical Flow Implementation**:
  - Use optical flow algorithms (e.g., Lucas-Kanade method) to detect and measure the movement of the camera.
  - Adjust player tracking data to account for camera movements, ensuring accurate player movement analysis.

### 5. Player Movement Measurement
- **Perspective Transformation**:
  - Apply perspective transformation techniques to convert pixel coordinates to real-world coordinates.
  - Measure player movement in meters rather than pixels for accurate distance and speed calculations.

### 6. Performance Metrics Calculation
- **Speed and Distance**:
  - Compute each player's speed by analyzing frame-to-frame movement.
  - Calculate the total distance covered by each player during the match.

## Conclusion
This project integrates state-of-the-art machine learning and computer vision techniques to deliver comprehensive football match analysis. By detecting and tracking players, classifying teams, and measuring performance metrics, it provides valuable insights into game dynamics and player efficiency. The use of YOLO, K-means clustering, optical flow, and perspective transformation showcases a powerful combination of technologies, making this project a versatile tool for sports analytics.



