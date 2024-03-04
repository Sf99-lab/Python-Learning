string = "A quick brown fox jumps over the lazy dog."

# 1. Now you print the string obtained by taking strides of 2 from the beginning
# 2. Strides of 4 starting from the 10th character till the end
# 3. Try printing using negative indices with strides of 2 till index -10

string_strides_2 = string[::2]
print(f"Strides of 2 from the beginning: {string_strides_2}") 

from_10th_character_strides_4 = string[9::4]
print(f"Strides of 4 from the 10th character: {from_10th_character_strides_4}") #For the stride of 4 start from 10th character and going till end

negative_indices_strides_2 = string[:-10:-2]
print(f"Negative indices with strides of 2: {negative_indices_strides_2}") #For the stride of 2 for negtive index

