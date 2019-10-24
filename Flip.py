import random
import matplotlib.pyplot as plt
import time


def flip():
    print('number of flips: ')
    num = input()
    startTime = time.time()

    try:
        num = int(num)
    except ValueError:
        print("not a valid number, try again")
        flip()

    if type(num) != int or num <= 0:
        print('Not a valid number, try again.')
        flip()

    head = 0
    for each in range(num):
        head += random.randint(0, 1)
    print('head: ' + str(head))
    print('tail: ' + str(num - head))

    endTime = time.time()
    total = round(endTime - startTime, 4)
    print('%s secs to flip %s coins' % (total, num))

    # graphing
    names = 'Head', 'Tail'
    scores = [head, num-head]
    percent = [head/num*100, (num-head)/num*100]

    fig, axs = plt.subplots(2)
    fig.suptitle('%s Flips \n %s Heads vs %s Tails' % (num, head, num-head))
    axs[0].bar(names, scores, align='center', alpha=0.5, color='red')

    axs[1].pie(percent, labels=names, startangle=90, autopct='%1.0f%%')
    axs[1].axis('equal')
    axs[1].set_xlabel('%s seconds' % total)
    plt.subplots_adjust(bottom=0.04, hspace=0.3)
    plt.show()

    flip()

if __name__ == '__main__':
    flip()
