import os
import shutil
source_folder="Images"
destination_folder="Moved_Images"

if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

    for file in os.listdir(source_folder):
        if file.endswith(".jpg"):
            old_path=os.path.join(source_folder,file)
            new_path=os.path.join(destination_folder,file)
            shutil.move(old_path,new_path)
        print(file,"moved")

print("Done! All .jpg files have been moved to the destination folder." )
