import os
import subprocess
files = os.listdir("videos")

for file in files:
    # Split around "Tutorial #"
    if "Tutorial #" in file:
        tutorial_number=file.split(".")[0].split("#")[1]
        file_name=file.split(" _ ")[0]
        print(file_name,tutorial_number)       
        subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])