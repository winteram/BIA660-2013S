import pygal 
radar_chart = pygal.Radar()
radar_chart.title = 'multi-dimentional analysis'
radar_chart.x_labels = ['Market', 'Hardware', 'Software', 'Appearance', 'Competitor']
radar_chart.add('GalaxyS3', [1378.0/5871, 1680.0/5871,1062.0/5871,2847.0/5871,244.0/5871])
radar_chart.add('Iphone', [889.0/5583, 1046.0/5583, 488.0/5583,667.0/5583,322.0/5583 ])

radar_chart.render_to_file('bar_chart.svg') 
