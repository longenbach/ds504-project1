# 12 digits

# a = "844349020387"
# s = (int(a[0]) + int(a[2]) + int(a[4]) + int(a[6]) + int(a[8]) + int(a[10]))*3 + (int(a[1]) + int(a[3]) + int(a[5]) + int(a[7]) + int(a[9]))
# print(s)
# print(a[11])
# print(10 - s%10)

def produce_last_digit(a):
    s = (int(a[0]) + int(a[2]) + int(a[4]) + int(a[6]) + int(a[8]) + int(a[10]))*3 + (int(a[1]) + int(a[3]) + int(a[5]) + int(a[7]) + int(a[9]))
    if(s%10 == 0):
        return "0"
    else:
        return str(10 - s%10)
