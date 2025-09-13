n1= float(input('First proof note : '))
n2= float(input('Second proof note : '))
m = float(n1+n2)/2

print('Your final note is {:1f}'.format(m))

print('Congratulations' if m >=6 else 'Please study more!')