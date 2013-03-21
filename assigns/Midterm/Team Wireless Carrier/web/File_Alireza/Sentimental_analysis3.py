from pychartdir import *
#The data for the pie chart
data = [292,197,169,103,103,71,56,54,51,69]

#The labels for the pie chart
labels = ["android", "trial" ,"update" ,"video" ,"frame" ,"window" ,"upgrade" ,"bean" ,"jelly" ,"smart"]

#Create a PieChart object of size 360 x 300 pixels
c = PieChart(360, 300)

#Set the center of the pie at (180, 140) and the radius to 100 pixels
c.setPieSize(180, 140, 100)

#Add a title to the pie chart
c.addTitle("Software- Galaxy")

#Draw the pie in 3D
c.set3D()

#Set the pie data and the pie labels
c.setData(data, labels)

#Explode the 1st sector (index = 0)
c.setExplode(0)

#output the chart
c.makeChart("new3.png")
