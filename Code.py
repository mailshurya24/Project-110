import statistics as sts
import csv
import random
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
claps = df["claps"].to_list()

p_mean = sts.mean(claps)
p_stdev = sts.stdev(claps)

def random_num(counter):
    data = []

    for i in range(0, counter):
        r_data = random.randint(0, len(claps))
        value = claps[r_data]
        data.append(value)

    d_mean = sts.mean(data)
    d_stdev = sts.stdev(data)

    return d_mean

def show_fig(means):
    var = means
    m_mean = sts.mean(means)
    m_stdev = sts.stdev(means)

    fig = ff.create_distplot([var], ["Number of Claps Received"], show_hist = False)
    fig.show()

    print(m_mean)
    print(m_stdev)

def setup():
    mean_list = []

    for i in range(0,100):
        setof_means = random_num(30)
        mean_list.append(setof_means)

    show_fig(mean_list)

setup()