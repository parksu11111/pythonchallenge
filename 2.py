from collections import Counter   //collection모듈의 Counter함수 
a= open("파일경로",'r')     //파일을 읽기모드(r)로 오픈한다.
b=a.read()              //읽어서 b에 저장한다.    파일로 저장안할시에는 b= '''복잡한문자열''' 이렇게
print(Counter(b))       // Counter을 사용해 문자의 개수를 출력한다.

