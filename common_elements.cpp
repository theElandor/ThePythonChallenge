#include <iostream>
#include <ctime>
#include <bits/stdc++.h>
using namespace std;
void d(int arr[] , int len)
{
	  for(int i = 0 ; i < len  ; i++)
	  {
		  cout<<arr[i]<<" ";
	  }
	  cout<<endl;
}
int min(int a , int b)
{
	if(a<b)
		return a;
	else
		return b;
}
int minim(int arr[] , int n, int indice)
{
    int res = indice;
    for(int i = indice+1 ; i < n ; i++)
    {
        if(arr[i] < arr[res])
            res = i;
    }
    return res;
}
void selection_rec(int arr[], int i , int n)
{
    if(i < n-1)
    {
        int k = minim(arr, n,i);
        swap(arr[i] , arr[k]);
        selection_rec(arr , i+1 , n);
    }
}
int main()
{
	int arr1[8];
	int arr2[6];
	srand(time(NULL));
	for(int i = 0 ; i < 8 ; i++)
	{
		arr1[i] = rand()%20;
	}
	for(int i = 0 ; i < 6  ;i++)
	{
		arr2[i] = rand()%20;
    }
    selection_rec(arr1 , 0 , 8);
    selection_rec(arr2 , 0 , 6);
	d(arr1,8);
	d(arr2, 6);
	int res[20];
	int k = 0;
	int i = 0;
	int j = 0;
	while(i<8 && j<6)
	{
		if(arr2[j] == arr1[i])
		{
			res[k] = arr2[j];
			k++;
            if(i == 7)
                i++;
            else if( j == 5)
                j++;
            else if(arr2[j+1] == arr1[i])
                i++;
            else
                j++; // indifferente
		}
		if(arr2[j] < arr1[i])
			j++;
		else
			i++;
	}
    d(res , k);
	return 0;
}
