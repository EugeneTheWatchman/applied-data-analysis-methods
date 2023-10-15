import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def readData():
    data = pd.read_table("Swiss Bank Notes.dat", sep=' ', decimal=',', engine='c')
    return data


def plot1(data):
    #fig = plt.figure(tight_layout=True)
    plt.title('''Построить гистограмму распределения для переменной
     длина банкноты''')
    #gs = gridspec.GridSpec(2, 2)

    #ax = fig.add_subplot(111)
    counts, bins = np.histogram(data['Length'])
    plt.hist(bins[:-1], bins, weights=counts)
    #ax.grid()
    plt.show()


def plot2(real, fake):
    fig = plt.figure(tight_layout=True)
    # plt.title('''построить отдельно гистограммы для
    # этой переменной по настоящим и фальшивым банкнотам,
    # изобразив на одном графике разным цветом''')
    gs = gridspec.GridSpec(2, 2)

    # real
    # ax = fig.add_subplot(gs[0, :])
    # counts, bins = np.histogram(real)
    # ax.hist(bins[:-1], bins, weights=counts)
    # ax.grid()
    # # fake
    # ax = fig.add_subplot(gs[1, :])
    # counts, bins = np.histogram(fake)
    # ax.hist(bins[:-1], bins, weights=counts)
    # ax.grid()
    # plt.show()

    ax = fig.add_subplot(gs[:, :])
    # real
    numberOfBins = int(1 + np.ceil(3.322 * np.log10(len(real))))
    counts, bins = np.histogram(real, numberOfBins)
    ax.hist(bins[:-1], bins, weights=counts, color='b', alpha=0.5, linewidth=0)
    ax.grid()
    # ax.hist(bins[:-1], bins, weights=counts, facecolor='None', edgecolor='k', linewidth=1)
    # fake
    numberOfBins = int(1 + np.ceil(3.322 * np.log10(len(fake))))
    counts, bins = np.histogram(fake, numberOfBins)
    ax.hist(bins[:-1], bins, weights=counts, color='r', alpha=0.5, linewidth=0)
    # ax.hist(bins[:-1], bins, weights=counts, facecolor='None', edgecolor='k', linewidth=1)
    plt.show()


def plot3(data, columns):
    fig = plt.figure(tight_layout=True)
    # plt.title('''Построить диаграммы  рассеивания по двум координатам
    # (длина диагонали+каждая другая) отображая  фальшивые и
    # подлинные банкноты разным цветом''')
    gs = gridspec.GridSpec(2, 3)
    diagonal = data['Diag']
    sublotX = 0
    sublotY = 0
    for column in columns[0:len(columns)]:
        ax = fig.add_subplot(gs[sublotX, sublotY])
        ax.scatter(diagonal[0:100], data[column][0:100], color='b', marker='+', s=50)
        ax.scatter(diagonal[100:200], data[column][100:200], color='r', marker='x', s=45)
        sublotX += 1
        if sublotX == 2:
            sublotX = 0
            sublotY += 1

    plt.show()


def plot3_1(data, columns):
    fig = plt.figure(tight_layout=True)
    # plt.title('''Построить диаграммы  рассеивания по двум координатам
    #     (каждая + каждая другая) отображая  фальшивые и
    #     подлинные банкноты разным цветом''')
    gs = gridspec.GridSpec(5, 5)
    diagonal = data['Diag']
    sublotX = 0
    sublotY = 0
    for column in columns[0:len(columns)]:
        for column2 in columns[0:len(columns)]:
            if sublotY > sublotX:
                ax = fig.add_subplot(gs[sublotX, sublotY-1])
                ax.scatter(data[column2][0:100], data[column][0:100], color='b', marker='+', s=50)
                ax.scatter(data[column2][100:200], data[column][100:200], color='r', marker='x', s=45)
            sublotX += 1
            if sublotX == 6:
                sublotX = 0
                sublotY += 1

    plt.show()

def plot4(real, fake):
    fig = plt.figure(tight_layout=True)
    # plt.title('''Построить гистограмму распределения для переменной длина
    # диагонали отдельно для фальшивых и подлинных банкнот''')
    gs = gridspec.GridSpec(2, 2)

    ax = fig.add_subplot(gs[:, :])
    # real
    numberOfBins = int(1 + np.ceil(3.322 * np.log10(len(real))))
    counts, bins = np.histogram(real, numberOfBins)
    ax.hist(bins[:-1], bins, weights=counts, color='b', alpha=0.5, linewidth=0)
    # ax.hist(bins[:-1], bins, weights=counts, facecolor='None', edgecolor='k', linewidth=1)
    # fake
    numberOfBins = int(1 + np.ceil(3.322 * np.log10(len(real))))
    counts, bins = np.histogram(fake, numberOfBins)
    ax.hist(bins[:-1], bins, weights=counts, color='r', alpha=0.5, linewidth=0)
    # ax.hist(bins[:-1], bins, weights=counts, facecolor='None', edgecolor='k', linewidth=1)
    ax.grid()
    plt.show()

if __name__ == "__main__":
    data = readData()
    dataLength = data['Length']
    plot1(data)
    real = data['Length'][0:100]
    fake = data['Length'][100:200]
    plot2(real, fake)
    plot3(data, data.columns)
    plot3_1(data, data.columns)
    real = data['Diag'][0:100]
    fake = data['Diag'][100:200]
    plot4(real, fake)
