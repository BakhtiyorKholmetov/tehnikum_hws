s='Hello, world!'
print(s[s.rfind(' ')+1:]+s[s.find(' '):s.rfind(' ')+1]+s[:s.find(' ')])
