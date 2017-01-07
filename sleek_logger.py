from termcolor import colored

class SleekLogger(object):
	def __init__(self, *args, **kwargs):
		self.method_to_type = {
			'info': '[INFO] ', 'debug': '[DEBUG] ',
			'warning': '[WARNING] ', 'error': '[ERROR] ' 
			}
		self.method_to_color = {
			'info': 'white', 'debug': 'cyan',
			'warning': 'yellow', 'error': 'red'
			}

	def format_log_string(self, message, method='info'):
		if method not in self.method_to_type:
			self.format_log_string("Log Method: {0} not defined".format(str(method)), 'error')
			return
		ret_string = self.method_to_type[method] + message
		ret_color = self.method_to_color[method]
		print(colored(ret_string, ret_color))

SleekLogger().format_log_string('hello')
SleekLogger().format_log_string('oops', 'warning')
SleekLogger().format_log_string('oh no', 'error')
SleekLogger().format_log_string('writing', 'debug')
SleekLogger().format_log_string('lolcopter', 'poop')
