from pychartdir import *
#The data for the pie chart
data = [502,522,215,185,126,115,113,111,108,107,105,104,94,88,82,78,52,52 ,48,40]

#The labels for the pie chart
labels = ["case", "mini" ,"pack", "small" ,"cover", "red" ,"leather", "look","luxury", "fashion", "silver", "designe", "screen", "purple", "white", "skin", "color", "blue", "black", "resin"]

#Create a PieChart object of size 360 x 300 pixels
c = PieChart(600, 320)

#Set the center of the pie at (180, 140) and the radius to 100 pixels
c.setPieSize(300, 140, 150)

#Add a title to the pie chart
c.addTitle("Appearance- Galaxy")

#Draw the pie in 3D
c.set3D()

#Set the pie data and the pie labels
c.setData(data, labels)

#Explode the 1st sector (index = 0)
c.setExplode(0)

#output the chart
c.makeChart("new4.png")
