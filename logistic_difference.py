import matplotlib.pyplot as plt

class walk():
	def __init__(self, num_points = 300):
			self.num_points = num_points
			self.x_values= [0]
			self.y_values = [0.6]
			self.R_value = 3
	def fill_y(self):
		for n in range(1,self.num_points+1):
			next_y = (self.R_value*self.y_values[-1])*(1-self.y_values[-1])
			self.y_values.append(next_y)
	def fill_x(self):
		for n in range(1,self.num_points+1):
			self.x_values.append(n)


r = walk()
r.fill_x()
r.fill_y()
print(r.x_values)
print(r.y_values)

plt.scatter(r.x_values, r.y_values)
plt.show()

