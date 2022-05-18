# para importar a data e horario
#import datetime
#best way o melhor modo é usando from date time import datetime
from datetime import datetime
#Para não ter que ficar repitindo uma função muitas vezes definimos uma unica função.

def print_time():
    print ('task completed')
    print (datetime.now())
    print ()

first_name ="Susan"
print_time()

for x in range (0,10):
    print (x)
print_time()
