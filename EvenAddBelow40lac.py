class EvenNumAdd:
    def method1(self):
        j=1
        i=0
        k=0
        result=0
        lo=0

        #for i in range(i,number):
        while j<=4000000:
            temp=k+j
            k=j
            j=temp
            if j<=4000000:
                if j%2==0:
                    print(temp)
                    result=result+j

            else:
                break


        print("value: " + str(result))

def main():
   # num=int(input("enter range"))
    en=EvenNumAdd()
    en.method1()

if __name__=='__main__':
    main()

