#!/usr/bin/env python
# encoding: utf-8

class BinarySearch(list):
    def __init__(self, a, b):
    	self.a = a # length of the list
    	self.b = b # difference between consecutive values
    	variablelength = 1 # search_value of elements in the array
        generated_list = []
        generated_list.append(b)
        for num in generated_list:
        	if variablelength < a:
        		generated_list.append(generated_list[variablelength -1] + b)
        		variablelength += 1

        		
        super(BinarySearch, self).__init__(generated_list)
        self.length = len(generated_list)

    def search(self, search_value):
        count = 0
        top_of_list = 0
        self.length = len(self)
        bottom_of_list = self.length - 1
        middle_of_list = int((bottom_of_list) / 2)
        position = {'count': '', 'index': ''}
        while top_of_list < middle_of_list: # Binary search algorithm
            if (top_of_list == middle_of_list) and (self[top_of_list] > search_value):
                index = -1
                position["count"] = self.length
                position["index"] = index
                return position
            elif self[top_of_list] == search_value:
                index = top_of_list
                position["count"] = count
                position["index"] = index
                return position
            elif self[bottom_of_list] == search_value:
                index = bottom_of_list
                position["count"] = count
                position["index"] = index
                return position
            elif self[middle_of_list] == search_value:
                index = middle_of_list
                position["count"] = count
                position["index"] = index
                return position
            else:
                if self[middle_of_list] > search_value:
                    bottom_of_list = middle_of_list - 1
                    top_of_list = top_of_list + 1
                    middle_of_list = (bottom_of_list + top_of_list) // 2
                else:
                    top_of_list = middle_of_list + 1
                    bottom_of_list = bottom_of_list - 1	
                    middle_of_list = ((bottom_of_list + top_of_list) // 2) + 1
            count += 1
        position = {'count': count, 'index': -1}
        return position

