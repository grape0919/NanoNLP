from os import lseek
from konlpy.tag import Kkma

kk = Kkma()
print(kk.pos(' 나는 학생으로서 학교생활을 하며 교칙에 묶여서 생활하는 것에 대한 불만을 품었다.', False, True))