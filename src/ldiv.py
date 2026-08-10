# binary Long Division of the unsigned integer with remainder (modulus)
# taken from the `https://en.wikipedia.org/wiki/Division_algorithm`
# Python Language Version
# Project Crew™ 8/4/2026

sub2  = '\u2082'
sub10 = '\u2081\u2080'
DivisionByZeroException: int = 1

def error(Error):
  if Error == 1 :
    print('Cannot divide by zero')
  else:
    print('Error occurred')
  exit(1)

def st(n: str) -> str:
  return('  Step {:<3} '.format(n + ':'))

def divide_unsigned(N: int, D: int) -> str:
  if D == 0 : error(DivisionByZeroException)
  print('\n  N = ', format(N, 'b'), sub2,
        ' (', N, sub10, ') and D = ', format(D, 'b'), sub2,
        ' (', D, sub10, '), ', sep='', end='')
  n:  int = 0
  ns: int = N
  while ns:              # Find highest set bit
    ns >>= 1
    n   += 1
  print(' #bits n =', n, end='\n\n')
  Q:  int = 0            # Initialize quotient and remainder to zero
  R:  int = 0
  print(st('1'), 'R =', R, 'and Q =', Q)
  for i in reversed(range(n)):   # Where n is number of bits in N
    print(st('2'), 'i =', i)
    R <<= 1              # Left-shift R by 1 bit
    print(st('3'), 'R = {0:0{n}b}'.format(R, n=n))
    if N & (1 << i):
      R |= 1
    else:
      R &= -2
    print(st('4'), 'R = {0:0{n}b}'.format(R, n=n))
    # R(0) = N(i)        # Set the least-significant bit of R equal to
    if R >= D:           #   bit i of the numerator
      print(st('5'), 'R \u2265 D, statement entered')
      R -= D
      print(st('5b'), 'R = {0:0{n}b}'.format(R, n=n))
      Q |= (1 << i)
      print(st('5c'), 'Q = {0:0{n}b}'.format(Q, n=n), end='\n\n')
      # Q(i) = 1
    else:
      print(st('5'), 'R \u2265 D, statement skipped', end='\n\n')
  return('(Q = {}, R = {})'.format(Q, R))

# main()
print('  Result:', divide_unsigned(12, 4), end='\n\n')
