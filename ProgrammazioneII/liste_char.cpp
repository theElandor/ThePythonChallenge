#include <iostream>
#include <cstring>
using namespace std;
const int buffer = 10;
struct elem
{
    char inf[buffer];
    elem* pun;
};
typedef elem * lista; // da ora se scrivo lista in realtÃ  sto dicendo elem*
char* head(lista p){return p->inf;}
lista tail(lista p){return (p->pun);}

void stampa_lista(lista p)
{
    while(p != NULL)
     {
        cout<<head(p)<<" "<<tail(p)<<endl;;
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
    lista testa = NULL;
    for(int i = 0 ; i < n ; i++)
    {
        elem *p = new elem;
        cout<<"Inserire nome: "<<endl;
        cin>>p->inf;
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

elem * search(lista l , char val[])
{
    while(l !=  NULL)
    {
        if(strcmp(head(l),val))
            return l;
        else
            l = tail(l);
    }
    return NULL; //se non trova niente ritorna NULL
}

int conta2 (lista l , char *val) // fuinfnzione di conta personalizzata
{   
    int counter = 0;
    while(l != NULL)
    {
        if(strcmp(head(l),val))
            counter++;
        l = tail(l);
    }
    return counter;
}

int conta(lista l, char *val) // funzione conta del prof
{
    int counter = 0;
    while((l=search(l , val)) != NULL)
    {
        l = tail(l); // aumento l e ri-inizio a contare dal secondo elemento
        counter ++;
    }
    return counter;
}
lista cancella(lista l , char *val) // cancella tutte le occorrenze di val
{ 
    elem* e; //variabile d'appoggio dove mi salvo l'indirizzo della variabile da cancellare
    while((e = search(l , val)) != NULL) // finchÃ¨ non ci sono piÃ¹ occorrenze
        l = delete_elem(l , e);
    return l;
    // cercare di rifare la funzione ma piÃ¹ efficente
}

lista cancella2(lista l , char *val) // DEBUG : ha problemi di segmentation fault
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

lista delete_tail_elem(lista testa)
{
    // controllo per un elemento
    lista partenza = testa;
    if(tail(testa) == NULL)
    {
        delete testa;
        return NULL;
    }
    while(tail(tail(testa)) != 0)
    {   
        testa = tail(testa);
    }
    lista appoggio = tail(testa);
    testa->pun = NULL;
    delete appoggio;
    return partenza;
}
lista tail_insert_elem(lista testa, char *val)
{
    lista partenza = testa;
    while(tail(testa) != NULL)
        testa = tail(testa);
    lista nuovo = new elem; // ricordarsi di allocare sempre
    cout<<"Sono arrivato a : "<<head(testa)<<endl;
    strcpy(nuovo->inf,val);
    nuovo->pun = NULL;
    testa->pun = nuovo;
    return partenza;
}

lista unione(lista testa1 , lista testa2)
{
    lista partenza = testa1;
    while(tail(testa1) != NULL)
    {
        testa1 = tail(testa1);
    }
    testa1->pun = testa2;
    return partenza;
}   

lista intersect(lista testa1 , lista testa2)
{
    int counter =0;
    lista testa3 = new elem;
    lista partenza = testa3;
    lista appoggio = testa2;
    // soluzione in costo quadratico
    while(testa1 != 0)
    {
        testa2 = appoggio;
        while(testa2 !=0 )
        {
            if(head(testa2) == head(testa1))
            {
                counter++;
                if(counter == 1) // stiamo allocando la testa
                   strcpy(testa3->inf,head(testa1));
                else
                {
                    if(head(testa3) != head(testa1)) // per non prendere 2 volte
                    {
                    lista elemento = new elem;
                    testa3 -> pun = elemento;
                    strcpy(elemento->inf ,head(testa1));
                    testa3 = tail(testa3);
                    }
                }
                break;
            }
            else
                testa2 = tail(testa2);
        }
        testa1 = tail(testa1);
    }
    cout<<"Counter : "<<counter<<endl;
    if(counter != 0)
        return partenza;
    else
    {
        delete testa3;
        return NULL;
    }
}
lista insert_ord(lista l , elem *e)
{
    lista partenza = l;
    if (strcmp(head(e), head(l))<0)
    {
        e->pun = l;
        return e;
    }
    else
    {   
        bool trovato = false;
        while(tail(l) != NULL && !trovato)
        {
            if(strcmp(head(l), head(e))<0 && strcmp(head(e), head(tail(l)))<0)
            {
                trovato = true;
                cout<<l<<" "<<tail(l)<<endl;
            }
            else
                l = tail(l);
        }
        e->pun = tail(l);
        l->pun = e;
    }
    return partenza;
}
int main()
{
    cout<<"Inserire il numero di elementi: ";
    int n;
    cin>>n;
    lista testa;
    lista persona;
    testa = crea_lista(n);
    cout<<"Lista attuale: ----------------"<<endl;
    stampa_lista(testa);
    cout<<"------------------------------"<<endl;
    persona = crea_lista(1);
    cout<<"Ho creato una persona da inserire: "<<persona<<endl;
    testa = insert_ord(testa , persona);
    cout<<endl;
    cout<<"Lista finale:-----------------"<<endl;
    stampa_lista(testa);
    cout<<"------------------------------"<<endl;
}


// zorro varret matteo capitani
