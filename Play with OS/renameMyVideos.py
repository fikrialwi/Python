import os
import glob
class RenameMyVideos:
    def __init__(self, folder):
        self.folder = folder
    def selectVideos(self):
        os.chdir(self.folder)
        return glob.glob("*.mp4") + glob.glob("*mkv")

    def removeNonVideos(self):
        file = os.listdir(self.folder)
        extVideos = [".mkv", ".mp4"]
        for i in file:
            if self.ext(i) not in extVideos:
                os.remove(f"{self.folder}\{i}")
            else:
                pass
        

    def ext(self, filename):
        file_name, file_extension = os.path.splitext(filename)
        return file_extension

    def numberingEps(self,n):
        n = n+1
        if len(str(n)) < 2:
            return "0"+str(n)
        return str(n)

    def renameVideos(self,newName):
        for i, oldName in enumerate(self.selectVideos()):
            dst = f"{self.folder}\{newName} eps - {self.numberingEps(i)}{self.ext(oldName)}"
            src = f"{self.folder}\{oldName}"
            try:
                os.rename(src, dst)
                print(f"video sudah direname dengan {dst}")
            except FileExistsError:
                print("Rename gagal")
    
# def main():
#     print("---Rename Videos---")
#     folder = input("input folder: ")
#     newName = input("input new name for file: ")
#     program = RenameMyVideos(folder)
#     program.removeNonVideos()
#     program.renameVideos(newName)
def main(folder, newName):
    print("---Rename Videos---")
    program = RenameMyVideos(folder)
    program.removeNonVideos()
    program.renameVideos(newName)
    

