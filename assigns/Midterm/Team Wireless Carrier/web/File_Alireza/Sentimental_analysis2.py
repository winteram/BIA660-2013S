from pychartdir import *
#The data for the pie chart
data = [196,223, 110, 102, 95, 76, 66, 40, 117,353]

#The labels for the pie chart
labels = ["prize","user","chance","free","buy","person","commercial","sale","coming","win"]

#Create a PieChart object of size 360 x 300 pixels
c = PieChart(360, 300)

#Set the center of the pie at (180, 140) and the radius to 100 pixels
c.setPieSize(180, 140, 100)

#Add a title to the pie chart
c.addTitle("Market- Galaxy")

#Draw the pie in 3D
c.set3D()

#Set the pie data and the pie labels
c.setData(data, labels)

#Explode the 1st sector (index = 0)
c.setExplode(0)

#output the chart
c.makeChart("new1.png")
