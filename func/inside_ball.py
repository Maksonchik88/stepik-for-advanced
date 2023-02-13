abscissas = list(map(float, input().split()))
ordinates = list(map(float, input().split()))
applications = list(map(float, input().split()))
print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applications))))