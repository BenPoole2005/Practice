from Tkinter import *
from functools import partial


class App:

	def __init__(self, master):

		self.master = master

		self.frame = Frame(master, height=10)
		self.frame.pack()

		self.button = []

		self.button.append(Button(self.frame, text="Play", command=self.start))
		self.button.append(Button(self.frame, text="Quit", command=self.frame.quit))

		for b in self.button:
			b.pack(side=LEFT)


	def start(self):
		self.options()
		self.buildMap()
		self.play()
		return

	def options(self):
		self.clear()
		self.button.append(Button(self.frame, text="Easy", command=partial(self.setup, "easy")))
		self.button.append(Button(self.frame, text="Medium", command=partial(self.setup, "medium")))
		self.button.append(Button(self.frame, text="Hard", command=partial(self.setup, "hard")))
		self.button.append(Button(self.frame, text="Imposible", command=partial(self.setup, "imp")))

		for b in self.button:
			b.pack(side=LEFT)

		self.frame.pack()



		return
	def setup(self, setting):
		return

	def buildMap(self):
		return

	def play(self):
		return

	def clear(self):
		for b in self.button:
			b.pack_remove()
		b = []



root = Tk()

app = App(root)

try:
	root.mainloop()
except KeyboardInterrupt:
	root.destroy()



