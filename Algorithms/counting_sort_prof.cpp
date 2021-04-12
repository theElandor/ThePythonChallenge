void counting(int arr[], int n , int k)
{
    int j;
    int C[k+1]; // indici da 0 a k
    for(int i = 0 ; i <= k ; i++)
    {
        C[i] = 0;
    }
    for(j = 0 ; j < n ; j++)
    {   
        C[arr[j]]++;
    }
    j = 0;
    for(int i = 0 ; i <= k ; i++)
    {
        while(C[i] > 0)
        {
            arr[j] = i;
            j++;
            C[i]--;
        }
    }
}
