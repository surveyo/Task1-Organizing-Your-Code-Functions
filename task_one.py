def plot_data(my_file):
    '''
    This function plots a scatterplot provided with a coordinate text file path 

    Parameters
    ----------
    my_file : STRING 
        Required path to the file with coordinates in text format 

    Returns
    ---------
    Scatterplot import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(
	'x_y_coordinates.txt', 
	delimiter=',', 
	header=None, 
	names=['x', 'y']
)
print("Column names:", data.columns)
plt.scatter(data['x'], data['y'])
plt.title('Scatter Plot of Coordinates')
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.grid(True)
plt.show()
    '''
    scatter_plot = None 
    """
    ==> Write your code here <==
    """
    return scatter_plot 
