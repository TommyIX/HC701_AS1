import nibabel as nib
import matplotlib.pyplot as plt

data = nib.load('Data/task_2/CT/study_0302.nii').get_fdata()

# Create the GUI
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

# Create the initial image plot
current_slice = 0
image = ax.imshow(data[:,:,current_slice], cmap='gray')

# Create the update function for scrolling
def update_slice(val):
    global current_slice
    current_slice = int(val)
    image.set_data(data[:,:,current_slice])
    fig.canvas.draw_idle()

# Create the scroll bar
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = plt.Slider(ax_slider, 'Slice', 0, data.shape[2] - 1, valinit=current_slice, valstep=1)
slider.on_changed(update_slice)

# Create the hover functionality
def hover(event):
    if event.inaxes == ax:
        x, y = int(event.xdata), int(event.ydata)
        z = current_slice
        value = data[y, x, z]
        fig.canvas.toolbar.set_message(f'Pixel location: ({x}, {y}, {z})\nPixel value: {value}')


fig.canvas.mpl_connect('motion_notify_event', hover)
# Show the GUI
plt.show()