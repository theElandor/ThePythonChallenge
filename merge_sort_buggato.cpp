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
void mergesort(int arr[], int len)
{
    int n = len;
    if(n < 2)
        return;
    int mid = n/2;
    int left[mid];
    int right[n-mid];
    for(int i = 0; i < mid ; i++)
        left[i] = arr[i];
    for(int i = mid ; i< n; i++)
        right[i-mid] = arr[i];
    mergesort(left,mid);
    mergesort(right,n-mid);
    merge(left, right , arr);
}
int main()
{    
    int arr[n];
    srand(time(0));
    for(int i = 0 ; i < n ; i++)
    {
        arr[i] = rand()%10;
    }
    d(arr , n);
    cout<<"Array ordinato: "<<endl;
    mergesort(arr, n);
    return 0;
}
