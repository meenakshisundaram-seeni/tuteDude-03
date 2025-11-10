mport math
def calculations(num):
    sqrt = math.sqrt(num)
    log = math.log(num)
    sine = math.sin(log)
    return sqrt, log, sine

val = int(input('Enter a number: '))
print(f'Square Root: {calculations(val)[0]}')
print(f'Logarithm: {calculations(val)[1]}')
print(f'Sine: {calculations(val)[2]}')