#include <iostream>
#include <cstring>
#include <conio.h>

using namespace std;
/*Implement an algorithm to determine if a string has all
 * unique characters  What if you can not use additional data structures*/
int main() {
    char str[500];
    cout<< "Enter string";
    cin>>str;
    bool alpha_count[256], flag=false;
    for(int i=0;i<256;i++)
        alpha_count[i]=false;

    for(int i=0;i<strlen(str);i++)
    {
        if(alpha_count[int(str[i])])
        {flag=true;  break;}
        else
            alpha_count[int(str[i])]=true;
    }

    if(flag==true)
        cout<<"Characters are not unique";
    else
        cout<<"Characters are unique";
    getch();

    return 0;
}

/*
 * Enter string aruunima
aruunima
Characters are not unique
 */