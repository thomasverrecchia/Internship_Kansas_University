import matplotlib.pyplot as plt
import csv
from statistics import*

## DON'T CHANGE BETWEEN THE LINE
#######################################################################################################################

name_list = ["Amdahl","Communication","General","Roofline"]
p_list = [500,1000,1500,2000,2500,3000,3500,4000,4500,5000]
mu_list = [0.02,0.04,0.06,0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22,0.24,0.26,0.28,0.3,0.32,0.34,0.36,0.38]
n_list = [100,200,300,400,500,600,700,800,900,1000]
parameter_list = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

for name in name_list :
    Paper = [[] for i in range(11)]
    Min_time = [[] for i in range(11)]
    f = open(name+"/all.csv",newline='')
    reader = csv.reader(f)
    for row in reader :
        if row[0] != "density" :
            index = int(float(row[0])*10)
            Paper[index] += [float(row[1]) / float(row[3])]
            Min_time[index] += [float(row[2]) / float(row[3])]

    f.close()
    f = open(name+"/mean.csv",'w',newline='')
    writer = csv.writer(f)
    mean_Paper = []
    mean_Time = []
    for k in parameter_list:
        index = int(k*10)
        writer.writerow([k,mean(Paper[index]),mean(Min_time[index])])
        mean_Paper += [mean(Paper[index])]
        mean_Time += [mean(Min_time[index])]
    f.close()

#######################################################################################################################

    plt.plot(parameter_list,mean_Paper,label='Algo Paper')
    plt.plot(parameter_list,mean_Time,label='Min Time')
    plt.xlabel("Density")
    plt.legend()
    plt.ylabel("Normalized Makespan")
    plt.savefig("plot_7_"+name+".png")
    plt.show()