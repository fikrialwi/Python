import os
def data_anime(path_save, path_anime):
    file = open(path_save, "r+")
    list_anime = os.listdir(path_anime)

    file.seek(0, os.SEEK_END)
    file.write(f"directory->{path_anime}:")
    txt = "\n"
    for i in list_anime:
        txt += f"{i}\n"
    
    file.seek(0, os.SEEK_END)
    file.write(txt)
    file.close()
    file = open(path_save, "r")
    for i in file:
        print(i)

path_save = "C://Users/ADMIN/Desktop/Daftar Anime.txt"
path_anime = "E://Anime"
path_anime2= "K://My Drive/Anime"
data_anime(path_save=path_save, path_anime=path_anime)


