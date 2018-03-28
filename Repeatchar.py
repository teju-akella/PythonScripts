class RepeatChar:
    def method1(self):
        s="amphora"
        #ind=s.index("a",0,-1)
        #print ("index is at: ", ind)
        #ss=s.lstrip(s[ind])
        #print ("now string is: ", ss)
        #ind1=ss.index("a",0,len(ss))
        #print ("index is at: ", ind1+len(s[ind]))

        i=0
        for i in range(i,len(s)-1):
            #if s[i]=="a":
                #print("index is at: ", i)

            print("Index is at: ", s.index("a",i,len(s)))
            if s.index("a", i, len(s)) == len(s)-1:
                break
            else:
                i+=1



def main():
    r=RepeatChar()
    r.method1()

if __name__ == '__main__':
    main()