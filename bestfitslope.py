from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import random

def generator(number,range_,correlation,step=3):
    val=1
    xs=[i for i in range(number)]
    ys=[]
    for _ in range(number):
        y=random.randint(-range_,range_)
        ys.append(y+val)
        if correlation=="pos":
            val+=step
        elif correlation=="neg":
            val-=step
    return np.array(xs,dtype=np.float64),np.array(ys,dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
    m=(((mean(xs) * mean(ys))-mean(xs*ys))/((mean(xs)*mean(xs))-mean(xs*xs)))
    intercept=mean(ys)-m*mean(xs)
    return m,intercept

def squared_error(ys_orig,ys_line):
    return sum((ys_line-ys_orig)**2)

def coeff_of_det(ys_orig,ys_line):
    y_mean_line=[mean(ys_orig) for y in ys_orig]
    return (1-((squared_error(ys_orig,ys_line))/(squared_error(ys_orig,y_mean_line))))

xs,ys=generator(100,50,"pos",2)
m,b=best_fit_slope_and_intercept(xs,ys)

regression_line=[(m*x)+b for x in xs]
plt.scatter(xs,ys)
plt.plot(xs,regression_line)
plt.show()

print(coeff_of_det(ys,regression_line))