import math, sys
class Primefactorial:
    def method1(self,number):
        #k=600851475143
        m=math.sqrt(number)
        print(sys.getsizeof(number))


        for i in range(1,number ):
            if number%i==0:
                print("factor: "+str(i))
            else:
                pass
def main():
    pm=Primefactorial()
    pm.method1(775146)

if __name__=='__main__':
    main()