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
        first = 0
        self.length = len(self)
        last = self.length - 1
        mid_point = int((last) / 2)
        position = {'count': '', 'index': ''}
        while first < mid_point: # Binary search algorithm
            if (first == mid_point) and (self[first] > search_value):
                index = -1
                position["count"] = self.length
                position["index"] = index
                return position
            elif self[first] == search_value:
                index = first
                position["count"] = count
                position["index"] = index
                return position
            elif self[last] == search_value:
                index = last
                position["count"] = count
                position["index"] = index
                return position
            elif self[mid_point] == search_value:
                index = mid_point
                position["count"] = count
                position["index"] = index
                return position
            else:
                if self[mid_point] > search_value:
                    last = mid_point - 1
                    first = first + 1
                    mid_point = (last + first) // 2
                else:
                    first = mid_point + 1
                    last = last - 1
                    mid_point = ((last + first) // 2) + 1
            count += 1
        position = {'count': count, 'index': -1}
        return position

