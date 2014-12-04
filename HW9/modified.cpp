// E.S. Boese
// 11/9/2014
#include <iostream>
using namespace std;

void change(int *i, int *j)
{
int temp = *j;
 *j = *i;
*i = temp;
}


int *toplace(int *start, int *end)
{
    int *i = start, *j= end;

    while(i<=j)
    {
    for(; *i<=*start && i<=end; i++);
    for(; *j>=*start && start+1<=j; j--);   
    if (i<j) change(i++,j--); 
    }

    change(start,i-1); 
    return i-1;
}

void sort(int *start, int *end)
{
    if (start >= end) return;

    for(int *debug = start;debug<=end;debug++) std::cout<<*debug <<" ";
    std::cout<<std::endl;  //this and...

    int *temp = start;
    temp = toplace(start,end);

    for(int *debug = start;debug<=end;debug++) std::cout<<*debug <<" ";
    std::cout<<std::endl; //...this are only to "see under the hood"
    std::cout<<std::endl;

    sort(start,temp-1);
    sort(temp+1,end);
}
int main(int argc, char* argv[])
{
    int A[] = {5,14,8,12,1,2,11,15,6,9,7,3,13,4,10};
    int n = sizeof (A) / sizeof(A[0]);

    sort(A, &A[n-1]);

    for (int i =0; i<n; i++) std::cout<<A[i] <<" ";

    return 0;
}