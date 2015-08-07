class FileSystem:
	def __init__(self):
		self.directory_array = []
		self.__setup_defaults()
		self.current_location = "/"

	def __setup_defaults(self):
		print "Setting up initial directories..."
		for each in "etc","lib","Users","home","bin","tmp":
			self.__mkdir(each)

	def __ls(self,directory = "./"):
		print self.directory_array

	def __pwd(self):
		print self.current_location

	def __cd(self,directory):
		self.current_location += (directory + "/")
		print self.current_location

	def __open(self,filename):
		pass

	def __mkdir(self,directory):
		self.directory_array.append({directory: []})

	def __help(self):
		print """
ls <directory_name>\t: DEFAULT = ./  Lists folder contents
cd <directory_name>\t: changes directories
open <filename>\t: opens file for viewing
pwd\t: prints working directory
help\t: prints help dialogue
setup-defaults\t: !! Erases your changes !! resets FileSystem to default structure. 
		"""

	def run_command(self,command):

		self.commands = {
			'ls' : self.__ls,
			'pwd': self.__pwd,
			'cd' : self.__cd,
			'open' : self.__open,
			'mkdir' : self.__mkdir,
			'help' : self.__help,
			'setup-defaults' : self.__setup_defaults
		}

		if command[1:] == []:
			self.commands[command[0]]()
		else:
			self.commands[command[0]](command[1])