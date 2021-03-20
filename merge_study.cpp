#include <iostream>
#include <ctime>
using namespace std;
const int n = 10;
const int ll = 5;
void swap(int &a , int &b)
{
    int t;
    t = a;
    a = b;
    b = t;
}
void d(int arr[], int len)
{
    for(int i = 0 ; i < len ; i++)
        cout<<arr[i]<<" ";
    cout<<endl;
}
void insertion(int arr[], int len)
{
    for(int i = 1 ; i < len; i++)
    {
        int temp = arr[i];
        int j = i;
        while(j>0 && arr[j-1]> temp)
           { arr[j] = arr[j-1];
            j--;}
        arr[j] = temp;
    }
}
void merge(int L[],int R[],int arr[])
{
    
}
int main()
{    
    int arr[ll];
    srand(time(0));
    for(int i = 0 ; i < ll ; i++)
    {
        arr[i] = rand()%10;
    }
    insertion(arr, ll);
    d(arr, ll);
    int arr2[ll];
    for(int i = 0 ; i < ll ; i++)
    {
        arr2[i] = rand()%10;
    }
    insertion(arr2, ll);
    d(arr2, ll);
    return 0;
}
