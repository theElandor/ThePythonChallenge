lista dealloca_ultimo(lista testa)
{
    lista partenza = testa;
    if(tail(testa)== NULL)
    {
        delete testa;
        partenza = NULL;
    }
    else
    {
        while(tail(tail(testa)) != NULL)
            testa = tail(testa);
        delete(tail(testa));
        testa->pun = NULL;
    }
    return partenza;
}
