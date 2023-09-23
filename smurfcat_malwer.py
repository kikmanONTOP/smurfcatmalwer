import os
import platform
import subprocess

def open_image(image_path):
    system = platform.system()

    if system == "Darwin":
        subprocess.run(["open", image_path])
    elif system == "Windows":
        os.startfile(image_path)
    else:
        try:
            subprocess.run(["xdg-open", image_path])
        except FileNotFoundError:
            print("sorry your os is stupid and cant open the image :(")


image_path = "we-live-we-love-we-lie.webp"


for _ in range(1000):

    open_image(image_path)


    subprocess.run(["sleep", "1"])

for i in range(222):
    print("WE LIVE WE LOVE WE LIE")