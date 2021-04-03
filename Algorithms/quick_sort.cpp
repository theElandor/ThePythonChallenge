int partition(int arr[], int p , int r)
{
    int x = arr[r]; // setto il pivot
    int i = p-1;
    for(int j = p; j<=r-1; j++)
    {
        if(arr[j] <= x)
        {
            swap(arr[j], arr[i+1]);
            i++;
        }
    }
    swap(arr[i+1], arr[r]);
    return i+1; // ritorno la posizione del pivot
}
void quicksort(int arr[], int p , int r)
{
    int q;
    if(p<r)
    {
        q = partition(arr, p , r);
        quicksort(arr, p ,q-1);
        quicksort(arr, q+1, r);
    }
}
