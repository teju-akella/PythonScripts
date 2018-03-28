import shutil,os

class FileOperations:
    def method1(self,oldfile,newfile):
        os.rename(oldfile,newfile)
        print("renamed sucessfully")
    def method2(self):
        try:
            os.mkdir("D:\\Teju\\python_Practice\\Practice_Stuff\\to")
            print("Directory created")
            self.reuse()
        except FileExistsError:
            print("directory already there")
            self.reuse()

    def reuse(self):
        srcfolder="D:\\Teju\\python_Practice\\Practice_Stuff\\from\\FBPriceTermPanel.nib"
        source = os.listdir(srcfolder)
        if (source != []):
            i = 1
            for files in source:
                print("in for loop file "+str(i) + ": " + files)
                i+=1
                if(files.endswith(".nib")):
                    shutil.copy(srcfolder+"\\"+files,"D:\\Teju\\python_Practice\\Practice_Stuff\\to")

                else:
                    print("no .nib type files")
            print("copied files")
        else:
            print("directory is empty")


def main():
    fo=FileOperations()
    #old = input("enter present file name")
    #newf = input("enter the desired file name to change")
    fo.method2()
   # fo.method1(old,newf)



if __name__ == '__main__':
    main()
