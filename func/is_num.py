# st not st.isalpha()
# st.upper() == st.lower()
# not st.count('.') > 1
# not st.count('-') > 1
# '0123456789.-' in st
# st.replace('-', '')


is_num = lambda x: "-" not in x[1:] and x.replace('.', '', 1).replace("-",'').isdigit()

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))