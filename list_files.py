import os,glob
def find_dir(path,type):
    os.chdir(path)
    return glob.glob("*."+type)

find_dir("E:\\","java")
find_dir("E:\\","txt")
find_dir("C:\\PythonCourse","py")
