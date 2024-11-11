from requirements.prettytable import PrettyTable
from datetime import datetime
import math

table = PrettyTable(['a', 'b', 'c', 'f(c)', 'f(a)', 'f(b)', 'f(a) * f (c)', 'f(b) * f(c)'], )
table.min_width = 10

def f(x: float):
   return math.cos(x) ** 2 + math.sin(x) + 1
 
def find_root(a: float, b: float, epsilon: float):
    c = (a + b) / 2
    fc = f(c)
    table.add_row([round(a, 4), round(b, 4), round(c, 4), round(fc, 4), round(f(a), 4), round(f(b), 4), round(f(a) * f(b), 4), round(f(b) * fc, 4)])
    
    while math.fabs(fc) > epsilon:
      if f(a) * f(c) < 0:
        b = c
      else:
        a = c
        
      c = (a + b) / 2
      fc = f(c)
      table.add_row([round(a, 4), round(b, 4), round(c, 4), round(fc, 4), round(f(a), 4), round(f(b), 4), round(f(a) * f(b), 4), round(f(b) * fc, 4)])
    return c

result = round(find_root(-1, 0.75, 0.00001), 4)

print(table)
timestamp = datetime.today().strftime("%d_%m_%y__%H_%M_%S")

with open(f'./answers/{timestamp}', 'w') as file:
  file.write(str(table))

print(f"x = {result}")