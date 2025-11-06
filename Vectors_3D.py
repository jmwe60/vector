import matplotlib.pyplot as plt
import numpy as np
import numbers
from mpl_toolkits.mplot3d import axes3d
from vector import Vector

class cyclic_index_list(list):
    def __getitem__(self, key):
        if isinstance(key, str):
            for item in self:
                if hasattr(item, 'name') and item.name == key:
                    return item
            raise KeyError
        elif isinstance(key, int):
            if abs(key) >= len(self):
                key = key % len(self)
            return super().__getitem__(key)

        elif isinstance(key, slice):
            return super().__getitem__(key)

        else:
            raise NotImplemented

if __name__ == '__main__':

    #points list
    vectors_array = np.array([
    [0,2,0],
    [2,0,0],
    [0,0,4],
    [0,-2,0],
    [0,0,3],
    [-2,0,0],
    [-2,-2,-5],
    [0,2,0],
    [0,0,-2],
    [0,4,0]])

    #convert to vector objects
    vectors = []
    for row in vectors_array:
        vectors.append(Vector(row))

    #cyclic color list
    origin = Vector([0,0,0])
    x_data, y_data, z_data = [origin[0]], [origin[1]], [origin[2]]
    available_colors = ['black','blue','green','cyan','yellow','magenta','pink','orange','red','brown','gray']
    colors = cyclic_index_list(available_colors)

    #plot vectors
    ax = plt.axes(projection = '3d')
    for i in range(len(vectors)):
        z_data.append(vectors[i][2]+z_data[i])
        y_data.append(vectors[i][1]+y_data[i])
        x_data.append(vectors[i][0]+x_data[i])
        ax.plot(x_data[i:i+2],y_data[i:i+2],z_data[i:i+2], marker = '^', color = colors[i])
        if i == 0:
            colors.pop(0)

    #graph style
    ax.set_title(f'Vectors Quick Draw\n',fontname = 'Consolas', fontsize = 11)
    ax.set_zlabel('   z')
    ax.set_ylabel('\n   y')
    ax.set_xlabel('\n   x')
    if not (max(x_data) - min(x_data)) > 8:
        ax.set_xticks(np.arange(min(x_data),max(x_data)+1,1))
    else:
        ax.set_xticks([min(x_data),max(x_data)+1])

    if not (max(y_data) - min(y_data)) > 8:
        ax.set_yticks(np.arange(min(y_data),max(y_data)+1,1))
    else:
        ax.set_yticks([min(y_data),max(y_data)+1])

    if not (max(z_data) - min(z_data)) > 8:
        ax.set_zticks(np.arange(min(z_data),max(z_data)+1,1))
    else:
        ax.set_zticks([min(z_data),max(z_data)+1])
 
    ax.set_box_aspect([max(x_data)+1, max(y_data)+1, max(z_data)+1])
    labels_size = 7
    ax.tick_params(axis='x', labelsize=labels_size)
    ax.tick_params(axis='y', labelsize=labels_size)
    ax.tick_params(axis='z', labelsize=labels_size)
    ax.grid(False)

    #select theme
    selection = 'harvest'
    alpha = 0.9
    themes = {'harvest':['#41B993','#F1B35F','#EEEEEE'],
              'horizon':['#3E4551','#6BA8C8','#E57C68'],
              'sisu':   ['#ACE8F2','#1C5D89','#4EBCFF'],
              'autum':  ['#009B77','#008080','#98FF98'],
              'white':  ['#FFFFFF','#FFFFFF','#FFFFFF']}
    
    ax.xaxis.set_pane_color(themes[selection][0],alpha)
    ax.yaxis.set_pane_color(themes[selection][1],alpha)
    ax.zaxis.set_pane_color(themes[selection][2],alpha)
    #ax.set_axis_off()

    plt.show()
