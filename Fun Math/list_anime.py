import os
def data_anime(path_save, path_anime):
    file = open(path_save, "r+")
    list_anime = os.listdir(path_anime)

    file.seek(0, os.SEEK_END)
    file.write(f"directory->{path_anime}:")
    txt = ""
    for i in list_anime:
        txt += f"{i}/n"
    
    file.seek(4, os.SEEK_END)
    file.write(txt)
    file.close()

