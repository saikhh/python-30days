# # import re

# # txt = 'I love to teach python and javaScript'
# # match = re.match('I  to teach', txt, re.I)
# # print(match)  # None 
 

# import re

# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# # It returns an object with span and match
# match = re.search('first', txt, re.I)
# print(match)  # <re.Match object; span=(100, 105), match='first'>
# # We can get the starting and ending position of the match as tuple using span
# span = match.span()
# print(span)     # (100, 105)
# # Lets find the start and stop position from the span
# start, end = span
# print(start, end)  # 100 105
# substring = txt[start:end]
# print(substring)       # first 



import re


# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# # It returns list
# matches = re.findall('python', txt, re.I)
# print(matches)  # ['Python', 'python']


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)