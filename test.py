import re

data = "`report The thing dont work"

endresult = re.split(r'\w\s', data, 1)
print(endresult)