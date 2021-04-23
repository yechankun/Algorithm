cro_alphas = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']
input_str = input()
for cro_alpha in cro_alphas:
    input_str = input_str.replace(cro_alpha,'#')
print(len(input_str))
