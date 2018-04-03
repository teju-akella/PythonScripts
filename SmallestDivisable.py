class SmallDiv:
    def method1(self):
        # ##########################################
        # i=20
        # while(i>0):
        #     print("entering into if with i  " +str(i))
        #     if(i%20==0 and i%15==0 and i%12==0 and i%16==0 and i%18==0):# and i%19==0 and i%18==0 and i%17==0 and i%16==0 and i%7==0 and i%11==0 and i%12==0 and i%13==0 and i%15==0):
        #         print("in loop")
        #         print("value: "+str(i))
        #         break;
        #     else:
        #         i=i+1
        # #############################################

        y=10
        my_list=[]
        while(y>=10):
            print("-----------for Y value-------  "+str(y))
            for x in range(1,21):
                n=(2*y)*x
                my_list.append(n)
                print("for x value: "+str(x))
            print(my_list)
            if(my_list[0] is my_list[-1]):
                print("$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                break
            else:
                y=y+1
            my_list = []





def main():
    sd=SmallDiv()
    sd.method1()

if __name__=='__main__':
    main()
