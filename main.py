file = open('sonar_readings.txt', 'r+')
f2 = file.read()
f2 = f2.replace('\n', ',')
sonar = f2.split(',')
sonar.pop(-1)

sonar = [int(i) for i in sonar]

ans = 0

for i in range(len(sonar)):
    if sonar[i - 1] < sonar[i]:
        ans += 1

print(ans)