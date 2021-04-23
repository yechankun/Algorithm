char_to_num_dict = {chr(i):(i-59)//3 for i in range(ord('A'), ord('P'))}
adding_dict = {'PQRS':7, 'TUV':8, 'WXYZ':9}
extract_adding_dict = {char:i for chars, i in adding_dict.items() for char in list(chars)}
char_to_num_dict.update(extract_adding_dict)
                        
input_string = input()
answer = 0
for c in input_string:
    answer += char_to_num_dict[c]+1
print(answer)
