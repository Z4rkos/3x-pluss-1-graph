import matplotlib.pyplot as plt
import sys

def run():
    if len(sys.argv) != 2:
        print("Please input a positive number as an argument.")
        return
    try:
        num = int(sys.argv[1])
    except:
        print("Please input a positive number as an argument.")
        return
    if num < 0:
        print("Please input a positive number as an argument.")
        return
    plot(num)

def collatz(num):
    output = [num]
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            output.append(num) 
        else:
            num = (num * 3) + 1
            output.append(num)
    return output


def plot(num):
    y = collatz(num)
    x=[i for i in range((len(y)))]

    plt.plot(x,y, color="red", linewidth="1", marker="o", markerfacecolor="black", markersize=3)
    plt.title("3x + 1 Graph")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()



if __name__ == "__main__":
    run()
