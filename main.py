# lp3thw p. 142

def z():

  print("05 1")
  yield(1)

  print("08 a")
  yield('a')

  print("11 2")
  yield(2)

  print("14 end")
# end of function zzz()


print("18 start the for loop")
for i in z():
  print("20 i =", i)
