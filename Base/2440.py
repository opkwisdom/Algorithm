def point_stars(num):
    for i in range(num, 0, -1):
        print("*" * i)
    
while True:
    data = input()
    if data != "\n":
        print(data)
    else:
        break