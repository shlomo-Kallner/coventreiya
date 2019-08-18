
###########################################################
#      
#            Module Main
#
#
def main():
    print("begining module tests...")
    print("Onset parse string: \"(C2) C1 (C1) (C3) (S (S)) (\'ʕ̞\')\"")
    print("components being refered to according to the fallowing table: ")
    print(" 1 for C1 ")
    print(" 2 for C2 ")
    print(" 3 for C3 ")
    print(" 4 for S ")
    print(" 5 for \'ʕ̞\' ")
    print()
    input("press ENTER to continue.")
    print()
    t = gen_onsets()
    print("TThe total number cobination of onset types is: ", len(t) )
    for i in t:
        print(i)
    print()
    input("press ENTER to continue.")
    print()
    s = input("please enter a file name with path for output: ")
    t1 = gen_actual_onsets_to_file(s)
    print("The total number of actual onset options is: ", t1 )
    bol = Query_for_value("Input Y / y to display Onsets or N / n to not: ",
                          {"Y" : True,
                           "y" : True,
                           "N" : False,
                           "n" : False})
    while bol:
        qs1 = input("Input Y / y to display Onsets or N / n to not: ")
        
    print("printing all possible onsets for file ", s, " ...")
    encoding_='utf-8'
    f = open(s,encoding=encoding_)
    bol = True
    while f.readable() and bol:
        s1 = f.readline()
        if len(s1) > 0:
            print(s1)
        else:
            bol = False
    print()
    input("press ENTER to continue.")
    print()
        


if __name__ == "__main__":
    main()
    

