from urllib.request import urlopen

with urlopen('https://docs.python.org/3/tutorial/stdlib.html#operating-system-interface') as response:
    for line in response:
        line = line.decode('utf-8')
        if 'EST' in line or 'EDT' in line:
            print(line)