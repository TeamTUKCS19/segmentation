# train, test, valid를 위해 이미지 resize해주는 코드
import cv2
import os


def resize_images(input_folder, output_folder, target_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)
            resized_img = cv2.resize(img, target_size)
            cv2.imwrite(os.path.join(output_folder, filename), resized_img)


# 설정할 폴더 경로
train_folder = './train/images/'
valid_folder = './valid/images/'
test_folder = './test/images/'

# 출력 폴더 경로
resized_train_folder = './train/resized_images/'
resized_valid_folder = './valid/resized_images/'
resized_test_folder = './test/resized_images/'

# 목표 크기 (YOLOv8의 경우 640x640 권장)
target_size = (640, 640)

# 각 폴더의 이미지를 리사이즈
resize_images(train_folder, resized_train_folder, target_size)
resize_images(valid_folder, resized_valid_folder, target_size)
resize_images(test_folder, resized_test_folder, target_size)
