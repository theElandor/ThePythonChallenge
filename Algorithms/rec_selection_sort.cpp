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
