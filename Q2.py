import sys

s = [1, 2, 9, 10, 4]
B = [[(sys.maxsize,-1)], [(sys.maxsize,-1)], [(sys.maxsize,-1)], [(sys.maxsize,-1)], [(sys.maxsize,-1)]]


def build_B():  
    for i in range(len(s)):
        # מציאת המקסימום בתת המערך שאינו גדול מS
        maxi = -1
        j_maxi = -1
        for j in range(i):
            if B[j][0][0] > maxi and B[j][0][0]<= s[i]:
                maxi = B[j][0][0]
                j_maxi = j
        # נמצא מקסימלי
        if(maxi != -1):
            B[j_maxi+1].insert(0,(s[i],i))
        # לא נמצא מקסימלי
        else:
            B[0][0] = (s[i],i)


def restore_list():
    # מציאת האינדקס האחרון שאינו מקס-אינט
    x=0
    while (B[x][0][0]!= sys.maxsize):
        x = x+1
    x = x-1;


    # הדפסת האיברים
    last_print_indx = sys.maxsize
    for i in reversed(range(x+1)):
        for j in range(len(B[i])):
            if B[i][j][1] < last_print_indx:
                print(f" {B[i][j][0]}")
                last_print_indx = B[i][j][1]
                break


def main():
    build_B()
    restore_list()


main()
