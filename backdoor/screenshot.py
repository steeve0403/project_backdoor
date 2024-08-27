from PIL import ImageGrab

screenshot = ImageGrab.grab()
# screenshot.show()
screenshot.save('screenshot.png', "PNG")