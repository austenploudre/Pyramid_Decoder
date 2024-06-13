#Import decoder string
import string
test_text = open('decoder_txt.txt','r')
txt = test_text.read()

#Initializing variables
array = ([])
last_value = 0
add = 1
iteration = 0
decode_numbers = []
sliced = []
number_list = []
decode_list = []
number_keys = []
number_values = []
code_dict = {}
dict_list = []
message = ""

#Splitting by newline character and removing empty line at the end
txt_list = txt.split("\n")
last_element = txt_list[-1]
if last_element == "":   
    txt_list.remove(last_element)
    
#Split to include multiple digit numbers
for x in txt_list:
    x = x.split(" ")
    number_list.append(int(x[0]))

#Sorting list by ascending number order
lists = sorted(number_list)

#Appending numbers to array with n+1 in each iteration
for i in lists:
    if last_value < len(lists):
        array.append(lists[last_value:last_value+add])
        last_value_list = array[-1]
        last_value = last_value_list[-1]
        add +=1
        iteration += 1
        
    else:
        break

#Extracting last number in each row of array
for i in array:
    decode_numbers.append(i[-1])

#Extracting matching word/number items from text file and appending to decode_list
for x in txt_list:
    x = x.split(" ")   
    if int(x[0]) in decode_numbers:
        decode_list.append(x)
        
#Mapping key value pairs for sorting
for x in decode_list:
    number_keys.append(int(x[0]))
    number_values.append(x[1])
    
#Creating key value pairs for sorting
code_dict = {number_keys[i]: number_values[i] for i in range(len(number_keys))}   
sorted_dict  = dict(sorted(code_dict.items()))

#Converting back to list before splitting
for key in sorted_dict:
    dict_list.append(str(key) + " " + sorted_dict[key])

#Splitting items in list and appending word value to sliced            
for x in dict_list:    
    word_item = x.split(" ")
    sliced.append(word_item[1])

#Appending each item to final message string
for item in sliced:
   message = message + item + " "
    
print(message)

         

