'''
Created on Jan 1, 2015

@author: amarvignesh_r
'''
class Circle:
    def __init__(self):
        self.radius = 2
    def perimeter_circle(self):
        return 2*3.14*self.radius
    

c=Circle()
print(c.perimeter_circle())