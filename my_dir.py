import argparse
import os
import shutil
import datetime

from enum import Enum


class FileSystemItemType(Enum):
    DIR = 0
    FILE = 1    

class FileSystemItem:
    def __init__(self, path, size, datetime, item_type):
        self._path = path
        self._size = size
        self._datetime = datetime
        self._item_type = item_type

    def __eq__(self, obj):        
        if self._path != obj._path:
            return False
        if self._size != obj._size:
            return False
        if self._datetime != obj._datetime:
            return False
        if self._item_type != obj._item_type:
            return False
        
        return True

        # TODO: implementation for getters          
def create_file_system_item(path):
    # os.path.getsize(path) must be replaced in case path point does directory,
    #  must be distinguished between folder and file when asking about size
    item_type = FileSystemItemType.DIR if os.path.isdir(path) else FileSystemItemType.FILE
    item_size = os.path.getsize(path) if item_type == FileSystemItemType.FILE else get_dir_size(path)
    # item_size = os.path.getsize(path)
    item_datetime = datetime.datetime.utcfromtimestamp(os.path.getmtime(path))   
    item = FileSystemItem(path, item_size, item_datetime, item_type)

    return item   

# TODO: Try to write unit test for this function 
def iterate_over_items_on_path(path):
    # add check whether given path is path to directory
    # very first item is directory of interest itself
    items = [create_file_system_item(path)]

    # iterate over content of directory
    content = os.listdir(path)
    for item in content:
        item_path = os.path.join(path, item)
        items.append(create_file_system_item(item_path))

    return items

def get_dir_size(start_path = '.'):
    total_dir_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_dir_size += os.path.getsize(fp)
    return total_dir_size 

def print_to_cmd(items):
    message = ''
    for index, item in enumerate(items):
        total_size = 0
        if index == 0:
            total_size = item._size
        else:
            item_type_str = 'DIR' if item._item_type == FileSystemItemType.DIR else '   '
            item_date_time_str = item._datetime.strftime("%m/%d/%Y, %H:%M:%S")
            item_name_str = f'{item._path:20}'
            item_size_str = str(item._size) # equivalent f'{item._size}'

            message = message + \
                item_type_str + \
                '   ' + item_date_time_str + \
                '   ' + item_name_str + item_size_str + ' bytes' + '\n'   
    
    # message = message + f'Space taken: {total_size} Bytes\n'
    sum_size = 'Directory size is: ' + str(get_dir_size()) + ' bytes'
    print(message, sum_size)
    

def main():
    parser = argparse.ArgumentParser(description='Prints content of given directory.')
    parser.add_argument(
            'path',
            metavar='PATH',
            type=str,
            nargs='?',
            default='.',
            help='To specify path of folder to print its content'
        )    
    args = parser.parse_args()
    
    # logic and presentation are separated
    file_system_items = iterate_over_items_on_path(args.path)
    print_to_cmd(file_system_items)
  
if __name__ == "__main__":
    main()
    
    

 