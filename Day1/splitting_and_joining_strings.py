original_string = "We can split Strings in Python"

split_string = original_string.split() 
print("Here we go:", split_string)

rsplit_string = original_string.rsplit() 
print("Here we go with rsplit() function: ", rsplit_string)

joined_string_with_delimiter = ' '.join(rsplit_string)
print("join() with delimiter ' ':", joined_string_with_delimiter)