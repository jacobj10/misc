from termcolor import colored

import os

class SleekLogger(object):
	def __init__(self, name, save_conf=False, rfh=False, rfh_lines=10):
		self.name = name
		self.rfh = rfh
		self.rfh_lines = rfh_lines
		self.write_mode = 0
		if self.rfh:
			self.rfh_WRITE = open(name, 'a')
			self.rfh_READ = open(name, 'r') # I ain't using rotatingfilehandler
		self.method_to_type = {
			'info': '[INFO] ', 'debug': '[DEBUG] ',
			'warning': '[WARNING] ', 'error': '[ERROR] ' 
			}
		self.method_to_color = {
			'info': 'white', 'debug': 'cyan',
			'warning': 'yellow', 'error': 'red'
			}
		self.valid_colors = ['grey', 'red', 'green', 'yellow', 'blue',
								'magenta', 'cyan', 'white']

	def add_log_method(self, method, color='white'):
			if color not in self.valid_colors:
				self.log("Color: {0} not valid".format(str(color)), 'error')

	def log(self, message, method='info'):
		if method not in self.method_to_type:
			self.log("Log Method: {0} not defined".format(str(method)), 'error')
			return
		ret_string = self.method_to_type[method] + message
		ret_color = self.method_to_color[method]
		if self.rfh:
			lines = [line for line in self.rfh_READ]
			num_lines = 1 + sum(1 for line in lines)
			if num_lines >= self.rfh_lines:
				if self.write_mode == 0:
					self.change_write_mode()
					self.write_mode = 1
				to_write = ''.join(lines[1:] + [ret_string,])
			else:
				to_write = ret_string + '\n'
			self.rfh_WRITE.write(to_write)
			print(num_lines)
		print(colored(ret_string, ret_color))

	def change_write_mode(self):
		self.rfh_WRITE.close()
		self.rfh_WRITE = open(self.name, 'w')

	def cleanup(self):
		self.rfh_READ.close()
		self.rfh_WRITE.close()
