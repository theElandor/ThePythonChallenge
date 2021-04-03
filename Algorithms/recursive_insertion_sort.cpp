void rec_insertion(int arr[], int n)
{
    if(n<=1)
        return;
    rec_insertion(arr , n-1);
    int temp = arr[n-1]; // al primo ciclo n = 2
    int j = n -2;
    while(j>= 0 && arr[j] > temp)
    {
        arr[j+1] = arr[j];
        j--;
    }
    arr[j+1] = temp;
}
