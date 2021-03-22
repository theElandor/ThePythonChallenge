int binary_search(int arr[], int key , int i , int j)
{
    cout<<"Chiamata"<<endl;
    if( i > j )
        return -1;
    int mid = (i+j)/2;
    if(arr[mid] == key)
        return mid;
    if (arr[mid] > key)
        return binary_search(arr ,key , i, mid-1);
    else
        return binary_search(arr, key , mid+1 , j);
}
