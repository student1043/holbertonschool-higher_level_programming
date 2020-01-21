#!/usr/bin/python3
class MyList(list):
    """This is a class MyList"""
    def print_sorted(self):
        """This is a definition"""
        SortedList = self.copy()
        SortedList.sort()
        print(SortedList)
