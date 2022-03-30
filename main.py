import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

population_mean = statistics.mean(data)
stdev = statistics.stdev(data)

#Population - the real data - raw data
#Sample - Small part of the population that can represent the population
print(population_mean,stdev)

# code to show the plot of raw data
#fig = ff.create_distplot([data], ["temp"], show_hist=False)
#fig.show()

#RANDOM SAMPLING

#code to find mean and std deviation of 100 data points - 1 sample
def sample_stats():
    dataset = []
    for i in range(0, 100):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    stdev = statistics.stdev(dataset)
    return [mean,stdev]

#1000 samples
def setup():
    mean_list=[]
    stdev_list=[]
    for a in range(0,1000):
        mean_list.append(sample_stats()[0])
        #stdev_list.append(sample_stats()[1])
    #showfig(mean_list)
    mean=statistics.mean(mean_list)
    #stdev_mean=statistics.mean(stdev_list)
    print(mean)

def showfig(mean_list):
    mean = statistics.mean(mean_list)
    fig=ff.create_distplot([mean_list],['sampling mean'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode='lines',name='mean'))
    
    fig.show()


setup()