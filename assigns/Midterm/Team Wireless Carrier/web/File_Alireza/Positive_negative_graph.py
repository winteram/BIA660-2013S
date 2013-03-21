from pychartdir import *
#The data for the pie chart
data = [85, 213, 150, 0,70,87]

#The labels for the pie chart
labels = ["positiveG4", "positiveG3" ,"positiveiP5" ,"negativeG4" ,"negativeG3" ,"negativeiP5"]

#Create a PieChart object of size 360 x 300 pixels
c = PieChart(360, 300)

#Set the center of the pie at (180, 140) and the radius to 100 pixels
c.setPieSize(180, 140, 100)

#Add a title to the pie chart
c.addTitle("Phone sentimental analysis")

#Draw the pie in 3D
c.set3D()

#Set the pie data and the pie labels
c.setData(data, labels)

#Explode the 1st sector (index = 0)
c.setExplode(0)

#output the chart
c.makeChart("threedpie.png")
