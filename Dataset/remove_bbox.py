import os


# 행을 삭제하고 파일을 다시 작성하는 함수 정의
def process_text_files(folder_path):
    text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    x = []
    for file in text_files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # 5개의 데이터를 가진 행을 삭제한 후 나머지 행을 유지
        new_lines = [line for line in lines if len(line.split()) != 5]

        # 파일 내용 갱신
        with open(file_path, 'w') as f:
            f.writelines(new_lines)

        # 만약 파일이 비어있으면 삭제
        if not new_lines:
            x.append(file)  # 리스트 x에 파일명 추가
            os.remove(file_path)  # txt 파일 삭제

    return x


def delete_matching_images(image_folder, x):
    for file in x:
        image_file = os.path.splitext(file)[0] + '.jpg'  # 이미지 파일 확장자
        image_path = os.path.join(image_folder, image_file)
        if os.path.exists(image_path):
            os.remove(image_path)


# 폴더 경로 설정
label_path_test = './test/labels/'
label_path_train = './train/labels/'
label_path_valid = './valid/labels/'

image_path_test = './test/images/'
image_path_train = './train/images/'
image_path_valid = './valid/images/'

# 각 폴더에 대해 처리
x_test = process_text_files(label_path_test)
x_train = process_text_files(label_path_train)
x_valid = process_text_files(label_path_valid)

delete_matching_images(image_path_test, x_test)
delete_matching_images(image_path_train, x_train)
delete_matching_images(image_path_valid, x_valid)
