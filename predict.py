import cv2
from ultralytics import YOLO
# 修改！！！！！！
# Load the YOLOv8 model
model = YOLO("./best.pt") # 自定义预测模型加载路径

# Open the video file
video_path = "./demo.mp4" # 自定义预测视频路径
cap = cv2.VideoCapture(video_path)

# Get the video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use lower case
out = cv2.VideoWriter('./output.mp4', fourcc, fps, (frame_width, frame_height)) # 自定义输出视频路径

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        # results = model(frame)
        results = model.predict(source=frame, save=True, imgsz=640, conf=0.6, show_conf=False) # 自定义输出预测结果路径

        # results[0].names[0] = "道路积水"
        # Visualize the results on the frame
        annotated_frame = results[0].plot(conf=False)

        # Write the annotated frame to the output file
        out.write(annotated_frame)

        # Display the annotated frame (optional)
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()