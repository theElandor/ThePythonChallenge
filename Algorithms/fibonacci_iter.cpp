int fib_iter(int n)
{
    if(n == 0 || n == 1)
        return 1;
    int s1 = 1;
    int s2 = 1;
    int res;
    for(int i = 0 ; i < n-1 ; i++)
    {
        res = s1+s2;
        s1 = s2;
        s2 = res;
    }
   return res;
}
