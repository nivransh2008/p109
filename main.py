import random 
import time 
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import pandas as pd 
dice_result = []
count = []
df = pd.read_csv("StudentsPerformance.csv")
for i in range(0,1000): 
    dice1 = random.randint(1,6) 
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2) 
    count.append(i) 
mean = sum(dice_result)/len(dice_result)
sd = statistics.stdev(dice_result) 
median = statistics.median(dice_result) 
mode = statistics.mode(dice_result)
firststd_start , firststd_end = mean - sd, mean + sd
secondstd_start,secondstd_end = mean - (2*sd), mean + (2*sd)
listofdatawithinonestandarddeviation = [result for result in dice_result if result>firststd_start and result<firststd_end   ]
print(sd,mean, median, mode) 
print("{}% of data lies withtin one standard deviaton".format(len(listofdatawithinonestandarddeviation)*100/len(dice_result)))
figure = ff.create_distplot([dice_result], ["result"]) 
figure.show()   