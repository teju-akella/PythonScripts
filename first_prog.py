class firstClass:
    def method1(self):
        print("1st method")

    def method2(self, something):
        print("something printing:" + something)

def main(c=firstClass()):
    c.method1()
    c.method2("teju")

if __name__ == '__main__':
    main()
