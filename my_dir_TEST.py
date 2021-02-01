import unittest
from my_dir import os, FileSystemItem, FileSystemItemType, create_file_system_item, get_dir_size, iterate_over_items_on_path
import unit_test_helpers
import datetime
from my_dir import __eq__

class TestMyDir(unittest.TestCase):
    count_set_up_call = 0
    count_set_up_class_call = 0

    def __init__(self, methodName='runTest'):        
        super().__init__(methodName)

    def setUp(self):
        TestMyDir.count_set_up_call = TestMyDir.count_set_up_call + 1
        print(f'\nNumber of setUP calls: {TestMyDir.count_set_up_call}')

    @classmethod
    def setUpClass(cls):
        # create folder structure on which we will test our code
        unit_test_helpers.create_folder_on_which_test_will_run()
        print(f'\nNumber of setUPClass calls: {TestMyDir.count_set_up_class_call}')

    @classmethod
    def tearDownClass(cls):        
        # we must clear everything we created which necessary to run our tests
        unit_test_helpers.delete_folder_on_which_test_will_run()

    def test_get_dir_size(self):       
        expected_size = 650
        actual_size = get_dir_size('./2')

        self.assertEqual(expected_size, actual_size)

    def test_create_file_system_item(self):
        # manually create item you expect, instead of question mark bellow
        path_to_file = './1/1'
        expected_item_datetime = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_to_file))   
        expected_item = FileSystemItem(path_to_file, 100, expected_item_datetime, FileSystemItemType.FILE)        
         # call function create_file_system_item(path) on path in our test folder to get actual value 
        actual_item = create_file_system_item(path_to_file)
        result = expected_item == actual_item 
        self.assertTrue(result)
        #create new path to file
    def test_iterate_over_items_on_path(self):
        # manual create items you expect
        # expected_items = ?
        # call function  iterate_over_items_on_path(path) to work on our test folders to get actual value 
        # actual_items = iterate_over_items_on_path(path)
        # iterate over items to check wherher they equals

        # path_1 = './1'
        # path_2 = './2'
        # path_3 = './1/1_1'
        # path_4 = './1/1_2'
        # path_5 = './2/1_1'
        path_dir_1 = './1'
        path_dir_2 = './2'

        path_date_1 = datetime.datetime.utcfromtimestamp(os.path.getmtime('./1'))
        path_date_2 = datetime.datetime.utcfromtimestamp(os.path.getmtime('./2'))
        # path_date_3 = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_3))
        # path_date_4 = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_4))
        # path_date_5 = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_5))
        # expected_items = [
        #     FileSystemItem(path_1, 100, path_date_1, FileSystemItemType.DIR),                        
        #     FileSystemItem(path_2, 0, path_date_2, FileSystemItemType.DIR), 
        #     FileSystemItem(path_3, 0, path_date_3, FileSystemItemType.DIR),
        #     FileSystemItem(path_4, 600, path_date_4, FileSystemItemType.DIR),
        #     FileSystemItem(path_5, 50, path_date_5, FileSystemItemType.DIR),
        #                  ]#+files

        expected_items = [
            FileSystemItem('./1', 100, path_date_1, FileSystemItemType.DIR), 
            FileSystemItem('./1/1_1', 0, path_date_1, FileSystemItemType.DIR), 
            FileSystemItem('./1/1_2', 0, path_date_1, FileSystemItemType.DIR),
            FileSystemItem('./1/1', 100, path_date_1, FileSystemItemType.FILE),
        ]              
        actual_items = iterate_over_items_on_path(path_dir_1)

        items_result = expected_items == actual_items
        self.assertFalse(items_result)

        expected_items = [
            FileSystemItem('./2', 650, path_date_2, FileSystemItemType.DIR), 
            FileSystemItem('./2/1_1', 50, path_date_2, FileSystemItemType.DIR),
            FileSystemItem('./2/1_1/1', 50, path_date_2, FileSystemItemType.FILE),
            FileSystemItem('./2/1', 100, path_date_2, FileSystemItemType.FILE),
            FileSystemItem('./2/2', 500, path_date_2, FileSystemItemType.FILE)
                         ]  
        actual_items = iterate_over_items_on_path(path_dir_2)

        items_result = expected_items == actual_items
        self.assertFalse(items_result)                 
        

    def test_FileSystemItem_eq(self):
        path_to_dir_1 = './1'
        dir_datetime_1 = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_to_dir_1))
        item_dir_1 = FileSystemItem(path_to_dir_1, 100, dir_datetime_1, FileSystemItemType.DIR)

        path_to_dir_2 = './1/1_1'
        dir_datetime_2 = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_to_dir_2))
        item_dir_2 = FileSystemItem(path_to_dir_2, 0, dir_datetime_2, FileSystemItemType.DIR)

        path_to_dir_3 = './1/1_2'
        dir_datetime_3 = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_to_dir_3))
        item_dir_3 = FileSystemItem(path_to_dir_3, 0, dir_datetime_3, FileSystemItemType.DIR)

        path_to_dir_4 = './2'
        dir_datetime_4 = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_to_dir_4))
        item_dir_4 = FileSystemItem(path_to_dir_4, 650, dir_datetime_4, FileSystemItemType.DIR)

        path_to_dir_5 = './2/1_1'
        dir_datetime_5 = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_to_dir_5))
        item_dir_5 = FileSystemItem(path_to_dir_5, 50, dir_datetime_5, FileSystemItemType.DIR)

        path_to_file_1 = './1/1'
        file_datetime_1 = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_to_file_1))
        item_file_1 = FileSystemItem(path_to_file_1, 100, file_datetime_1, FileSystemItemType.FILE)

        path_to_file_2 = './2/1_1/1'
        file_datetime_2 = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_to_file_2))
        item_file_2 = FileSystemItem(path_to_file_2, 50, file_datetime_2, FileSystemItemType.FILE)

        path_to_file_3 = './2/1'
        file_datetime_3 = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_to_file_3))
        item_file_3 = FileSystemItem(path_to_file_3, 100, file_datetime_3, FileSystemItemType.FILE)

        path_to_file_4 = './2/2'
        file_datetime_4 = datetime.datetime.utcfromtimestamp(os.path.getmtime(path_to_file_4))
        item_file_4 = FileSystemItem(path_to_file_4, 500, file_datetime_4, FileSystemItemType.FILE)
        # expected_result_after_equality_test = False
        # self.assertTrue(expected_result_after_equality_test == actual_result_after_equality_test) 
        #kazdy s kazdym
        items_dir_result_1 = item_dir_1 == item_dir_2
        items_dir_result_2 = item_dir_1 == item_dir_3
        items_dir_result_3 = item_dir_1 == item_dir_4
        items_dir_result_4 = item_dir_1 == item_dir_5
        items_dir_result_5 = item_dir_2 == item_dir_3
        items_dir_result_6 = item_dir_2 == item_dir_4
        items_dir_result_7 = item_dir_2 == item_dir_5
        items_dir_result_8 = item_dir_3 == item_dir_4
        items_dir_result_9 = item_dir_3 == item_dir_5
        items_dir_result_10 = item_dir_4 == item_dir_5
        self.assertFalse(items_dir_result_1)
        self.assertFalse(items_dir_result_2)
        self.assertFalse(items_dir_result_3)
        self.assertFalse(items_dir_result_4)
        self.assertFalse(items_dir_result_5)
        self.assertFalse(items_dir_result_6)
        self.assertFalse(items_dir_result_7)
        self.assertFalse(items_dir_result_8)
        self.assertFalse(items_dir_result_9)
        self.assertFalse(items_dir_result_10)
         

        items_file_result_1 = item_file_1 == item_file_2
        items_file_result_2 = item_file_1 == item_file_3
        items_file_result_3 = item_file_1 == item_file_4
        items_file_result_4 = item_file_2 == item_file_3
        items_file_result_5 = item_file_2 == item_file_4
        items_file_result_6 = item_file_3 == item_file_4
        self.assertFalse(items_file_result_1)
        self.assertFalse(items_file_result_2)
        self.assertFalse(items_file_result_3)
        self.assertFalse(items_file_result_4)
        self.assertFalse(items_file_result_5)
        self.assertFalse(items_file_result_6)
        #2 items 1 dir & 1 file
        item_dir_4_again = FileSystemItem(
                path_to_dir_4,
                650,
                dir_datetime_4,
                FileSystemItemType.DIR
            )
        self.assertTrue(item_dir_4 == item_dir_4_again)
        item_file_4_again = FileSystemItem(
            path_to_file_4,
            500,
            file_datetime_4,
            FileSystemItemType.FILE
            )
        self.assertTrue(item_file_4 == item_file_4_again)    
 
    
if __name__ == "__main__":
    unittest.main()        