import plotly.graph_objects as go

fig = go.Figure(data=
    go.Scatterpolar(r = [13.53, 48.45, 47.47, 88.84, 60.01, 128.42, 34.00, 54.84, 134.57, 123.58, 
 33.15, 79.73, 83.29, 53.67, 37.51, 53.70, 44.19, 125.19, 87.71, 49.57, 
 43.14, 131.29, 86.43, 47.57, 50.86, 135.40, 80.07, 40.26, 55.75],
        theta = [116.33,
                 108.66, 
                 108.42, 
                 114.97, 
                 112.54, 
                 124.64, 
                 120.00, 
                 113.65, 
                 121.84, 
                 122.01, 
                 104.86, 
                 115.64, 
                 115.23, 
                 115.37, 
                 121.32, 
                 110.72, 
                 109.84,
                 123.17,
                 116.04, 
                 117.00, 
                 115.39, 
                 123.78, 
                 114.25, 
                 116.87, 
                 113.15, 124.40, 117.52, 108.84, 105.61],
        mode =  'markers',        
    ))

fig.update_layout(showlegend=False)
fig.show()
     


r= [111.10, 87.57, 56.31, 68.44, 47.15, 101.57, 55.51, 72.55, 83.81, 48.78, 
 95.91, 78.63, 49.43, 66.46, 28.58, 77.89, 50.41, 50.48, 38.74, 32.08, 
 47.15, 38.43, 26.63, 40.63, 45.90, 28.16, 39.89, 82.83, 65.34, 69.20]