def find_max_min(list):
  max_min_equals = []
  if all(num == list[0] for num in list) == True:  
    max_min_equals.append(len(list))
    return max_min_equals
  else:  
    maximum = max(list)       
    minimum = min(list)
    max_min_list = []    
    max_min_list.append(minimum)
    max_min_list.append(maximum)    
    return max_min_list