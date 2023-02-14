from typing import *

def safe_password(st: str) -> bool:
    if st.islower() == False and st.isupper() == False and st.isdigit() == False and st.isalpha() == False and len(st) >= 7:
        return True

print('YES' if safe_password(input()) else 'NO')
