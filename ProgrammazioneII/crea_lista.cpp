lista insert_elem(lista l, elem* e)
{
    e-> pun = l;
    return e; // ritorno la nuova testa
}
lista crea_lista(int n)
{
    int val;
    lista testa = new elem;
    cin>>val;
    testa->inf = val;
    for(int i = 0 ; i < n-1 ; i++)
    {
        elem*p = new elem;
        cin>>val;
        p->inf = val;
        testa = insert_elem(testa , p);
    }
    return testa;
}
