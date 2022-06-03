import matplotlib.pyplot as plt
import sys


def run():
    arg_error = "Please input a positive number as an argument."
    if len(sys.argv) != 2:
        print(arg_error)
        return
    try:
        num = int(sys.argv[1])
    except:
        print(arg_error)
        return
    if num < 0:
        print(arg_error)
        return
    plot(num)


def collatz(num):
    output = [num]
    while num != 1:
        num = num / 2 if num % 2 == 0 else num * 3 + 1
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
