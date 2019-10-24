import random
import matplotlib.pyplot as plt


def flip():
    print('number of flips: ')
    num = int(input())

    if type(num) != int or num <= 0:
        print('Not a valid number, try again.')
        flip()

    head = 0
    for each in range(num):
        head += random.randint(0, 1)
    print('head: ' + str(head))
    print('tail: ' + str(num - head))

    # graphing
    names = 'Head', 'Tail'
    scores = [head, num-head]
    percent = [num/head*100, num/(num-head)*100]

    fig, axs = plt.subplots(2)
    fig.suptitle('Coin Flip')
    axs[0].bar(names, scores, align='center', alpha=0.5, color='red')
    for i, v in enumerate(scores):
        axs[0].text(v, i, str(v), color='blue', fontweight='bold')

    axs[1].pie(percent, labels=names, startangle=90, autopct='%1.0f%%')
    axs[1].axis('equal')
    plt.subplots_adjust(bottom=0.04, hspace=0.3)
    plt.show()

    flip()

if __name__ == '__main__':
    flip()
