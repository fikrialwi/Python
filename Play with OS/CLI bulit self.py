import argparse
import renameMyVideos as rv
parser = argparse.ArgumentParser(description="we will rename all your videos on folder")

parser.add_argument(
    'folder',
    type=str,
    help= "enter path directory of your videos"
    
)

parser.add_argument(
    '-nw',
    '--newName',
    type = str,
    help = "enter your new name for your videos"
)

folderPath = parser.parse_args().folder
newName = parser.parse_args().newName

rv.main(folder = folderPath, newName = newName)

