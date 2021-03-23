int MCD(int m , int n)
{
    if(n == m)
        return m;
    if(m > n)
        return MCD(m-n , n);
    else
        return MCD(m , n-m);
}
