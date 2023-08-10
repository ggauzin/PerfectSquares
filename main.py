from math import sqrt
import math
def main():
    num_qtt = math.floor(sqrt(1000000000))
    print(num_qtt)
    list = open("list.txt", "w")
    for i in range(num_qtt):
        list.write(str(i*i) + "\n")
    list.close()
if __name__ == '__main__':
    main()
