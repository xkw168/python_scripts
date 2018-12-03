from simpledbf import Dbf5
from os import walk, sep

if __name__ == "__main__":
    srcDir = r"C:\Users\xkw\Desktop\data\dbf"
    dstDir = r"C:\Users\xkw\Desktop\data\csv"
    for root, dirs, filenames in walk(srcDir):
        for file in filenames:
            if file.endswith(".dbf"):
                dbf = Dbf5(root + sep + file, codec='gbk')
                dbf.to_csv(dstDir + sep + file[:-4] + ".csv")
