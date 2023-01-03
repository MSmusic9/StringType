import time

def finder(text, list):
  if list.count(text) != 0:
    return True
  else:
    return False

def p(text):
  return "", text

def times(num, text):
  time.sleep(num)
  return text

def lock(key, file, value):
  f = open(file,"r")
  a = {key: value}
  if key == a.key(value):
    f.read()
    return a[key]

def check(text, check):
  text = str(text)
  return text.find(check)

def type(var):
	if var == str(var):
	  return True
	else:
		return False