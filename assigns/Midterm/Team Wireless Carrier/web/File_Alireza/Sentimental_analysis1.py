from pychartdir import *
#The data for the pie chart
data = [335,1115,57,51,46,40]

#The labels for the pie chart
labels = ["mobile","phone","feature","device", "camera","battery"]

#Create a PieChart object of size 400 x 300 pixels
c = PieChart(460, 380)

#Set the center of the pie at (300, 200) and the radius to 100 pixels
c.setPieSize(180, 140, 140)

#Add a title to the pie chart
c.addTitle("Hardware-Galaxy")

#Draw the pie in 3D
c.set3D()

#Set the pie data and the pie labels
c.setData(data, labels)

#Explode the 1st sector (index = 0)
c.setExplode(0)

#output the chart
c.makeChart("new2.png")
