void counting_sort(int arr[], int max)
{
    int times[max];
    azzera(times , max); // setta tutti i valori a zero
    for(int i = 0 ; i < n ; i++)
    {
        times[arr[i]]++;
    }
    d(times); // display
    int k = 0;
    while(k < n)
    {
        for(int j = 0 ; j < max ; j++)
        {
            if(times[j] != 0)
            {
                for(int i = 0 ; i < times[j]; i++)
                {
                    arr[k] = j;
                    k++;
                }
            }
        }
    }
    cout<<"Array ordinato: "<<endl;
    d(arr);
}
