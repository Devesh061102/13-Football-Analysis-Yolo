from ultralytics import YOLO

model = YOLO(r'models\best.pt')
results = model.predict('input_video\input.mp4',save = True,njobs = -1)
print(results[0])
print("====================")
for box in results[0].boxes:
    print(box)
    