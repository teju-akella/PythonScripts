import zipfile,os

# zip_ref = zipfile.ZipFile("D:\\Teju\\python_Practice\\Practice_Stuff\\Amphora.zip", "w")
# print("names are: "+str(zip_ref.namelist()))
# zip_ref.extractall("D:\\Teju\\python_Practice\\Practice_Stuff\\to")
# print("unzipped sucessfully")
#
# print(zipfile.is_zipfile("D:\\Teju\\python_Practice\\Practice_Stuff\\Amphora.zip"))

# zip_ref=zipfile.ZipFile("D:\\CircleK\\lib\\test.zip", "w")
# zip_ref.write("D:\\Teju\\python_Practice\\Practice_Stuff")
# zip_ref.close()

# zf = zipfile.ZipFile("D:\\Teju\\python_Practice\\Practice_Stuff\\to\\myzipfile.zip", "w")
# for dirname, subdirs, files in os.walk("D:\\Teju\\deployment\\new\\release_html\\issue"):
#     #zf.write(dirname)
#     for filename in files:
#         zf.write(os.path.join(dirname, filename))
#         print(os.path.join(dirname, filename))
# zf.close()

class zipper:
    def zipDir(self, dirPath, zipPath):
        zipf = zipfile.ZipFile(zipPath , mode='w')
        lenDirPath = len(dirPath)
        for root, _ , files in os.walk(dirPath):
            for file in files:
                filePath = os.path.join(root, file)
                zipf.write(filePath , filePath[lenDirPath :] )
        zipf.close()

def main():
    zp=zipper()
    zp.zipDir("D:\\Teju\\deployment\\new\\release_html\\issue" , "D:\\Teju\\python_Practice\\Practice_Stuff\\to\\zipper.zip")
if __name__ == '__main__':
    main()