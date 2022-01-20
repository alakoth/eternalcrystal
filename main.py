import random
def generate(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        var1 = random.choice(lines)
        var1 = var1.strip()
        var2 = random.choice(lines)
        var2 = var2.strip()
        codename = f'{var1+var2}'
        revcodename = f'{var2+var1}'
        print('CODENAME: ' + codename)
        print('ALTERNATE: ' + revcodename)