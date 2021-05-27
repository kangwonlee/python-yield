# lp3thw p. 142

def zzz():

  print("05 1")
  yield(1)

  print("08 a")
  yield('a')

  print("11 2")
  yield(2)


for i in zzz():
  print("16 i =", i)
