#!/usr/bin/python3

class Camera:
	def __init__(self, pixel, magnification):
		self.pixel = pixel
		self.magnification = magnification
	
	def takepicture(self):
		self.message = "Bad code"
		print("찰칵")
		print("사진이 저장되었습니다.(화소 {}만, 배율 {}x)".format(self.pixel, self.magnification))
		
if __name__ == "__main":
	cannon = Camera(2430, 1.0)
	cannon.takepicture()
	sony = Camera(2410, 3.0)
	sony.takepicture()

