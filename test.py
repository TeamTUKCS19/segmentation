from ultralytics import YOLO
import torch

# model = YOLO('..\server\yolov8n-seg.pt')
model = YOLO('./yolov8s_best2.pt')

# result = model.predict(source='./2.png', save=True)

COLOR_MAPPING = {
    'Crack': (0, 0, 255),  # 빨간색
}

CLASS_MAPPING = {
    0: 'Crack',
}
results = model.predict('./1.png')

for result in results:
    for r in result.boxes:
        box = r.xyxy.tolist()
        conf = r.conf.tolist()
        print(f'bbox : {box}')
        print(f'conf : {conf}')
        print(r.xyxy)
        print(r.conf)
        x1, y1, x2, y2 = map(int, box[0])
        print(x1,y1,x2,y2)


"""
    if results is None or len(results.xyxy[0]) == 0:
        return None
    for result in results.xyxy[0]:
        box = result[:4]  # 바운딩 박스의 좌표값 (x1, y1, x2, y2)
        label_index = int(result[5])
        label = CLASS_MAPPING.get(label_index, 'Unknown')  # 객체 클래스
        conf = result[4]  # 신뢰도
"""
