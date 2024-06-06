from ultralytics import YOLO

data_path = 'C:/TeamTUKCS19/segmentation/data.yaml'
epochs = 40
batch_size = 16

"""
if __name__ == '__main__':
    model = YOLO('./best.pt')
    model.train(data=data_path, epochs=epochs, batch=batch_size, device='0')
"""
model = YOLO('./best.pt')

results = model.predict("./crack_E.mp4", save=True, save_frames=True)

"""
for result in results:
    boxes = result.boxes
    mask = result.masks
    keypoints = result.keypoints
    probs= result.probs
    obb = result.obb
    result.show()
    print(boxes)
    print(mask)
    print(keypoints)
    print(probs)
    print(obb)
"""

