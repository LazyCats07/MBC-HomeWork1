import os

# Data
data = {
  'a' : int,
  'b' : int
}

# Functions
def add():
  return data.get('a') + data.get('b')

def substract():
  return data.get('a') - data.get('b')

def times():
  return data.get('a') * data.get('b')

def distribut():
    return data.get('a') / data.get('b')

# Start Here
print('\n\nSimple Kalkulator\n\n')
data['a'] = float(input('Bilangan 1\t: '))
data['b'] = float(input('Bilangan 2\t: '))

print('1.\tPenjumlahan\n2.\tPengurangan\n3.\tPerkalian\n4.\tPembagian\n5.\tBatal')

while True:
  op = input('Choose operation (Ex: 5)\t: ')

  match op:
    case '1':
      print('Jawaban\t: ', add())
    case '2':
      print('Jawaban\t: ', substract())
    case '3':
      print('Jawaban\t: ', times())
    case '4':
      print('Jawaban\t: ', distribut())
    case '5':
      os.system('cls')
      exit('Good Bye')
    case default:
      print('Error: Failed to locate index.')