# 기본 계산기
def add(a, b):
  return a+b

def subtract(a, b):
  return a-b

def multiply_(a, b):
  return a*b

def divide_new(a, b):
  return a/b

def get_Median(a, b):
    return (a+b)/2

def get_Remainder(a, b):
  return a % b

def get_Abs(a):
  if (a < 0):
    return -a
  else:
    return a

def get_Percent(a, b):
  return (a/b)*100

def get_Median(a, b):
    return (a+b)/2

def getSum_ver1(n):
    return n(n+1)/2

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num