#!/usr/bin/python3

# Solution for Mathe im Advent. 2020-12-20. Classes 7 to 9.
# https://www.mathe-im-advent.de/de/kalender/7-9/20/ .

import copy
import sys

class Field:
	def __init__(self, data):
		self.data = data

	def get(self, position):
		return self.data[position[1]][position[0]]

	def set(self, position, value):
		self.data[position[1]] = self.data[position[1]][:position[0]] + value + self.data[position[1]][position[0] + 1:]

class Robot:
	def __init__(self, position, direction):
		self.position = position
		self.direction = direction

	def right(self):
		self.direction=(-self.direction[1],+self.direction[0])

	def left(self):
		self.direction=(+self.direction[1],-self.direction[0])

	def go(self, step):
		self.position=(self.position[0] + self.direction[0] * step, self.position[1] + self.direction[1] * step)

class Logic:
	def __init__(self, field, robot):
		self.field = field
		self.robot = robot
		self.count = 0

	def print(self):
		for y in range(len(self.field.data)):
			for x in range(len(self.field.data[0])):
				if self.robot.position == (x,y):
					if self.robot.direction==(1,0):
						print('>', end='')
					elif self.robot.direction==(-1,0):
						print('<', end='')
					elif self.robot.direction==(0,-1):
						print('^', end='')
					elif self.robot.direction==(0,1):
						print('v', end='')
					else:
						print('R', end='')
				else:
					print(self.field.get((x,y)), end='')
			print()

	def scan_right(self):
		scan_robot=copy.copy(self.robot)
		scan_robot.right()
		scan_robot.go(1)
		return self.field.get(scan_robot.position)

	def scan_forward(self):
		scan_robot=copy.copy(self.robot)
		scan_robot.go(1)
		return self.field.get(scan_robot.position)

	def scan_left(self):
		scan_robot=copy.copy(self.robot)
		scan_robot.left()
		scan_robot.go(1)
		return self.field.get(scan_robot.position)

	def step(self):
		if self.scan_right() == '=':
			self.robot.right()
			self.robot.go(1)
			self.field.set(self.robot.position, ' ')
			self.count = 0
		else:
			if self.scan_forward() == '=':
				self.robot.go(1)
				self.field.set(self.robot.position, ' ')
				self.count = 0
			else:
				if self.scan_left() == 'X':
					self.robot.go(-1)
					self.count = 0
				else:
					self.robot.left()
					self.robot.go(1)
					self.field.set(self.robot.position, ' ')
					self.count = self.count+1
					if self.count == 4:
						sys.exit()

l=Logic(Field([
	'XXXXXXXXX',
	'X=======X',
	'X====X==X',
	'XX======X',
	'X==X====X',
	'X=======X',
	'XX=X====X',
	'XXXXXXX X',
	'XXXXXXXXX'
	]),Robot((7,7),(0,-1)))
l.print()
while True:
	input('')
	l.step()
	l.print()

