# Optimization in portfolio

### Introduction
Do not put eggs in the same basket is the truth in invest.<br>
How to choose between risk and profit is an important issue for investors.

### Problem
* dimension: number of stock
* constraint: expected return
* target: find portfolio weight such that mininize the risk

### Implement
$E(x)$
* expected return: ![](https://i.imgur.com/vB9RAh8.png)
* loss function: ![](https://i.imgur.com/qww1DCY.png)
* gradient of weight: ![](https://i.imgur.com/vLBjiXM.png)

### Flowchart
![flowchart](https://i.imgur.com/1Bx2utG.jpg)

### Experiment
Calculate the return rate of historical stock prices of MA (MasterCard) and PEP (Pepsi) then configure the best portfolio weights through return rate. In the future, you may use this weight to minimize risk. 

Parameter setting: 
* learngin rate = 1
* iteration number = 500000
* initial weight = [0.50, 0.50]
```
$ python3 main.py
available stock: ['BRK.B' 'CELG' 'DOW' 'EMR' 'HAL' 'MA' 'MRK' 'PEP' 'PM' 'SPG']
input stock_1: PEP
input stock_2: MA
input expect_return: 0.01
[iter 0]: var=0.011367093929764961
[iter 5000]: var=0.01132968038237862
...
[iter 495000]: var=0.010181078043472725
Variance of equal weight: 0.011367101464399985
Best weight with min variance: (0.45275093951586426, 0.5472490604841358)
```
![](https://i.imgur.com/wvIWcQa.png)

### Conclusion
Further compare with the configure of average weight, you can figure out that variacne is decreasing from 0.0114 to 0.0102. Althrough the reduction is not very large at first glance but you can reduce unnecessary risks when the amount of investment is large macroscopically.

### Reference
> [1] Modern portfolio theory and investment analysis
