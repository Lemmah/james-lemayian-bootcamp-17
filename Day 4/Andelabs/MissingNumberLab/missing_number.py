#!/usr/bin/env python
# encoding: utf-8

def find_missing(list1,list2):
	if isinstance(list1, list) and isinstance(list2, list):
		if len(list1) == 0 and len(list2) == 0:
			return 0
		elif list1 == list2:
			return 0
		else: # Using python sets to compare the lists			
			if_superset = set(list1).difference(list2)
			if_subset = set(list2).difference(list1)
			option1 = list(if_subset)
			option2 = list(if_superset)
			if len(option1) != 0:
				missing_number = option1[0]
				return missing_number
			else:
				missing_number = option2[0]
				return missing_number
		return missing_number
			
			
find_missing([1, 2], [1, 2, 5])