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
    int nL = 5;
    int nR = 5;
    int i = 0;
    int j = 0 ;
    int k = 0;
    while(i < nL && j < nR)
    {
        if(L[i] <= R[j])
        {
            arr[k] = L[i];
            k++;
            i++;
        }
        else
        {
            arr[k] = R[j];
            k++;
            j++;
        }
    }
    while(i < nL) // solo uno di questi due viene eseguito
    {
        arr[k] = L[i];
        i++;
        k++;
    }
    while(j < nR)
    {
        arr[k] = R[j];
        k++;
        j++;
    }
}
int main()
{    
    int arr[ll];
    int arr2[ll];
    int res[n];
    srand(time(0));
    for(int i = 0 ; i < ll ; i++)
    {
        arr[i] = rand()%10;
    }
    insertion(arr, ll);
    d(arr, ll);
    for(int i = 0 ; i < ll ; i++)
    {
        arr2[i] = rand()%10;
    }
    insertion(arr2, ll);
    d(arr2, ll);
    merge(arr , arr2 , res);
    d(res,n);
    return 0;
}
