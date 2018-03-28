class Multiple:
    def multiplication(self,number):
        i=1
        j=0
        for i in range(i, number):
            print("in for loop" + str(i))
            if i % 3 == 0 or i % 5 == 0:
                j = j+i
                print("value is: " + str(j))

            else:
                pass

def main():
    num=int(input("enter a number"))
    mu= Multiple()
    mu.multiplication(num)

if __name__ == '__main__':
    main()


