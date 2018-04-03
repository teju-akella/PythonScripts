import shutil,os
class LargestPalinrome:
    def method1(self):
        for i in range(100,999):
            for j in range(100,999):
                k=i*j
                m=str(k)[::-1]

                print(str(i)+"X"+str(j)+"="+str(k)+" reverse "+str(m))
                if(str(k)!=str(m)):
                    pass

                else:
                    print("Palindrome " + str(k))
                    break

def main():
    lp=LargestPalinrome()
    lp.method1()
if __name__=='__main__':
    main()


