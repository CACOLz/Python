import os
import shutil

# 파일이 위치한 디렉토리와 이동할 폴더 경로 설정
original_directory = "path_to_original_directory"  # 원본 파일이 위치한 디렉토리 경로
target_directory = "path_to_target_directory"  # 이동할 폴더 경로

# 디렉토리 설정
os.chdir(original_directory)

# 파일 목록 가져오기
file_list = os.listdir()

# 파일명 변경 및 이동
for file in file_list:
    # 파일명 변경 로직
    new_file_name = "new_" + file  # 새로운 파일명 설정

    # 파일 이동 로직
    file_path = os.path.join(original_directory, file)  # 파일의 전체 경로
    new_file_path = os.path.join(target_directory, new_file_name)  # 새로운 파일의 전체 경로

    # 파일 이동
    shutil.move(file_path, new_file_path)

