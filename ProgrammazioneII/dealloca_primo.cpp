lista dealloca_primo(lista testa)
{
    if(testa == NULL)
        return NULL;
    lista partenza = testa;
    testa = tail(testa);
    delete partenza;
    return testa;
}
