import re
a=open("D:\python_challenge\pythonchallenge3.txt",'r')
b=a.read()

pattern = re.compile("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]")
print("".join(re.findall(pattern,b)))   //문자열로 반환 문자열 사이에 "" 삽입



//'*print의 join
// 'print("구분자",join(list)) : list를 문자열로 반환 (문자열 사이에 구분자 삽입)
// 'print("구분자", join(string)) : 구분자를 기준으로 string을 끊어서 리스트로 반환
