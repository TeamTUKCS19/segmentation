# 이 파일은 Change_dataset.py로 인해 crack이 없어서 메모장에 아무것도 안쓰여져 있을경우 해당 이미지와 txt파일을 제거하기 위한 코드이다.

import os


label_path_test = './test/labels/'
label_path_train = './train/labels/'
label_path_valid = './valid/labels/'


image_path_test = './test/images/'
image_path_train = './train/images/'
image_path_valid = './valid/images/'


# 폴더 내의 텍스트 파일 목록을 반환
def get_text_files(folder_path):
    text_files = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            text_files.append(filename)
    return text_files


# 빈 텍스트 파일의 파일명을 반환
def find_empty_files(folder_path):
    empty_files = []
    text_files = get_text_files(folder_path)
    for filename in text_files:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            if not file.read().strip():
                empty_files.append(filename)
    return empty_files


# 이미지 파일들 중 빈 txt 파일명과 같은 파일은 삭제
def delete_matching_images(image_folder, labels_folder, file_names):
    for filename in file_names:
        image_path = os.path.join(image_folder, filename.replace('.txt', '.jpg'))  # 이미지 파일 확장자를 고려하여 수정
        if os.path.exists(image_path):
            os.remove(image_path)
        os.remove(os.path.join(labels_folder, filename))


# './test/labels/'에 있는 빈 텍스트 파일 찾기
empty_files_test = find_empty_files(label_path_test)
empty_files_train = find_empty_files(label_path_train)
empty_files_valid = find_empty_files(label_path_valid)

# './test/images/'에서 해당 텍스트 파일명과 동일한 이미지 파일 삭제
delete_matching_images(image_path_test, label_path_test, empty_files_test)
delete_matching_images(image_path_train, label_path_train, empty_files_train)
delete_matching_images(image_path_valid, label_path_valid, empty_files_valid)


print("Done.")
