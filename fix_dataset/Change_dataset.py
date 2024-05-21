import os


# 특정 datset 은 클래스가 4개이므로 Crack만이라도 제대로 탐지하기 위해 crack을 제외한 클래스는 제거
# crack을 세부분류한 것을 하나의 클래스로 병합하기 위한  .py이다.

# 폴더 경로 설정
folder_path_test = './test/labels/'
folder_path_train = './train/labels/'
folder_path_valid = './valid/labels/'


# 파일에서 값들 읽어옴
def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        # 문자열 float 값으로 변환
        row = [float(value) for value in line.strip().split()]
        data.append(row)
    return data


# 첫번째 값이 0.0과 1.0인 행 제거 # 첫번째 값이 data 클래스로 정수형 0~3이다. 하지만 float값으로 변환했기 때문에 0.0 1.0
def remove_rows_with_values(data, values_to_remove):
    return [row for row in data if row[0] not in values_to_remove]


# 첫번째 값이 3.0과 4.0인 값을 0으로 변경.
def replace_values(data, values_to_replace, new_value):
    for row in data:
        for i in range(len(row)):
            if row[i] in values_to_replace:
                row[i] = new_value
    return data


# 수정된 데이터를 파일 저장합니다
def write_data(file_path, data):
    with open(file_path, 'w') as file:
        for row in data:
            line = ' '.join(map(str, row))
            file.write(line + '\n')


# 폴더 내 모든 파일을 처리하는 함수
def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            # 데이터 읽기
            data = read_data(file_path)

            # 행 제거 및 값 변경
            data = remove_rows_with_values(data, values_to_remove={0.0, 1.0})
            data = replace_values(data, values_to_replace={3.0, 4.0}, new_value=0)

            # 데이터 저장
            write_data(file_path, data)
            print(f"{filename} 파일이 성공적으로 처리되었습니다.")


# 폴더 내 모든 파일 처리
process_folder(folder_path_test)
process_folder(folder_path_train)
process_folder(folder_path_valid)

