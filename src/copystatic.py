import os, shutil


def copy_files_recursive(source, destination):

    # Check if source directory exist 
    if not os.path.exists(source):
        raise Exception(f"Source directory: \"{source}\" does not exist.")   
    
    if os.path.exists(destination):
        shutil.rmtree(destination)
    
    # shutil.copytree exists but i want to work on recursion
    os.mkdir(destination)

    dir_names = sorted(os.listdir(source))
    dir_list = []
    file_list = []
    for name in dir_names:
        if os.path.isdir(source + "/" + name):
            dir_list.append(name)
        if os.path.isfile(source + "/" + name):
            file_list.append(name)

    for file in file_list:
        shutil.copy(source + "/" + file, destination + "/" + file)

    for dir in dir_list:
        os.mkdir(destination + "/" + dir)

        # recursion
        copy_files_recursive(source + "/" + dir, destination + "/" + dir)
