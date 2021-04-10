#include <iostream>
using namespace std;
struct elem
{
    int inf;
    elem* pun;
};
typedef elem * lista; // da ora se scrivo lista in realtà sto dicendo elem*
int head(lista p){return p->inf;}
lista tail(lista p){return (p->pun);}
void stampa_lista(lista p)
{
    while(p != NULL)
     {
        cout<<head(p)<<" ";
        p = tail(p); // avanzo nella lista
     }
     cout<<endl;
}
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
lista delete_elem(lista l , elem *e)
{   
    if(l == e)
        l = tail(l); // avanzo di uno per poi deallocare
    else
    {
        lista l1 = l; // mi salvo il punto di partenza
        while(tail(l1) != e)
        {
            l1 = tail(l1);
        }
        l1->pun = tail(e);    
    }
    delete e; // dealloco
    return l;
}
void eliminalista(lista &testa)
{
    while(testa!=NULL)
        testa = delete_elem(testa ,testa);
        // a ogni ciclo aggiorno la testa , quando la aggiorno a null allora mi fermo
}
elem * search(lista l , int val)
{
    while(l !=  NULL)
    {
        if(head(l) == val)
            return l;
        else
            l = tail(l);
    }
    return NULL; //se non trova niente ritorna NULL
}
int conta2 (lista l , int val) // fuinfnzione di conta personalizzata
{   
    int counter = 0;
    while(l != NULL)
    {
        if(head(l) == val)
            counter++;
        l = tail(l);
    }
    return counter;
}
int conta(lista l, int val) // funzione conta del prof
{
    int counter = 0;
    while((l=search(l , val)) != NULL)
    {
        l = tail(l); // aumento l e ri-inizio a contare dal secondo elemento
        counter ++;
    }
    return counter;
}
lista cancella(lista l , int val) // cancella tutte le occorrenze di val
{ 
    elem* e; //variabile d'appoggio dove mi salvo l'indirizzo della variabile da cancellare
    while((e = search(l , val)) != NULL) // finchè non ci sono più occorrenze
        l = delete_elem(l , e);
    return l;
    // cercare di rifare la funzione ma più efficente
}
lista cancella2(lista l , int val) // DEBUG : ha problemi di segmentation fault
{   
    while(head(l) == val)
    {  
        elem* partenza = l;
        l = tail(l); // avanzo di uno per poi deallocare
        delete partenza;
    }   
    lista l1 = l; // mi salvo il punto di partenza
    while(l1 != NULL)
    {
        if(tail(l1) != NULL && head(tail(l1)) == val)
        {
          l1->pun = tail(tail(l1));
          delete tail(l1);
          stampa_lista(l1);
        }
        else
            l1 = tail(l1);
    }   
    return l;
}
int lunghezza(lista l)
{
    if(tail(l) == NULL)
        return 1;
    else
        return(lunghezza(tail(l))+1);
}
int main()
{
    int n;
    cout<<"Inserire numero di elementi: ";
    cin>>n;
    lista testa = crea_lista(n);
    cout<<"Ecco la tua lista: "<<endl;
    stampa_lista(testa);
    cout<<"Lunghezza della lista: "<<lunghezza(testa)<<endl;
}
