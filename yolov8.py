from ultralytics import YOLO

data_path = 'C:/TeamTUKCS19/segmentation/data.yaml'
epochs = 40
batch_size = 16

if __name__ == '__main__':
    model = YOLO('yolov8n-seg.pt')
    model.train(data=data_path, epochs=epochs, batch=batch_size, device='0')
