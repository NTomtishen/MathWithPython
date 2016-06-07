import matplotlib.pyplot as plt
from matplotlib import animation

# Creates a circle and plots it
'''
def create_circle():
	circle = plt.Circle((0, 0), radius = 0.5, fc = 'g', ec = 'r')
	return circle

def show_shape(patch):
	ax = plt.gca()
	ax.add_patch(patch)
	plt.axis('scaled')
	plt.show()

c = create_circle()
show_shape(c)
'''

def update_radius(i, circle):
	circle.radius = i*0.5
	return circle,

def create_animation():
	fig = plt.gcf()
	ax = plt.axes(xlim = (-10, 10), ylim = (-10, 10))
	ax.set_aspect('equal')
	circle = plt.Circle((0, 0), 0.05)
	ax.add_patch(circle)
	anim = animation.FuncAnimation(
		fig, update_radius, fargs = (circle,), frames = 30, interval = 50)
	plt.title('Simple Circle Animation')
	plt.show()

create_animation()