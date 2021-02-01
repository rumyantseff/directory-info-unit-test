import os
import shutil

def create_dummy_test_file(path, size=10):
    data = bytearray(size) 
    with open(path, 'bw') as fs:
        fs.write(data)          
def create_folder_on_which_test_will_run():
    os.mkdir('./1')
    create_dummy_test_file('./1/1', 100)
    os.mkdir('./2')
    os.mkdir('./1/1_1')
    os.mkdir('./1/1_2')
    create_dummy_test_file('./2/1', 100)
    create_dummy_test_file('./2/2', 500)
    os.mkdir('./2/1_1')
    create_dummy_test_file('./2/1_1/1', 50)
def delete_folder_on_which_test_will_run():
  shutil.rmtree('./1')
  shutil.rmtree('./2')