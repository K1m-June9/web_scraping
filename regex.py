#정규식
import re

p = re.compile("ca.e")# p=패턴, .=하나의 문자를 의미 (ca.e) = cafe,cave,care,cade ..., 
#^=문자열의 시작(^de) = desk, desination fade(x)
# $(se$)  = 문자열의 끝 > case, base(o) | face(x)
#m = p.match("cavfe")
#print(m.group()) #매칭 실패 시 에러
def print_match(m):
    if m:
        print("group",m.group()) #일치하는 문자열 반환
        print("string",m.string)# 입력받은 문자열
        print("start",m.start())#일치하는 문자열의 시작 index
        print("end",m.end())# 일치하는 문자열의 끝 index
        print("span",m.span())#일치하는 문자열의 시작/끝 index
    else:
        print("매칭 실패")

#m = p.match("careless") # match: 주어진 문자열의 처음부터 일치하는지 확인(길이 안맞아도 됨, 뒤에 더 있어도 됨)
#print_match(m) 
        
# m = p.search("good care")#search: 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)
        
# lst = p.findall("careless")#findall: 일치하는 모든 것을 리스트 형태로 반환
# print(lst)
        
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열")
# 3. m = p.search("비교할 문자열")
# 4. lst = p.findall("careless") // "리스트" 형태로 반환
# 원하는 형태: 정규식
# p=패턴, .=하나의 문자를 의미 (ca.e) = cafe,cave,care,cade ..., 
#^=문자열의 시작(^de) = desk, desination fade(x)
# $(se$)  = 문자열의 끝 > case, base(o) | face(x)