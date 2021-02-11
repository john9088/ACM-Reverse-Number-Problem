def revNum(n):
  ans = 0
  while n != 0:
    temp = int(n%10)
    n = int(n/10)
    ans = ans*10 + temp 
  return(ans)


N = int(input("Enter Number of test Cases:"))
count = 0
while count < N:
  revAns = 0
  case = input(f"Case {count + 1}-> Enter two integers seprated by space:")
  a = list(map(int,case.split(" ")))

  #To find Reverse of Number and Add them
  revAns = revNum(a[0]) + revNum(a[1])

  #Reverse the final sum
  print(revNum(revAns))
  count += 1
