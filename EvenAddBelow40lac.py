class EvenNumAdd:
    def method1(self, number):
        j=2
        i=1
        k=0

        for i in range(i,number):
            temp=i+j
            i=j
            j=temp
            if j<=4000000:
                if i%2==0:
                    k=i+k
                else:
                    pass

            else:
                break


        print("value: " + str(k))

def main():
   # num=int(input("enter range"))
    en=EvenNumAdd()
    en.method1(4000000)

if __name__=='__main__':
    main()

