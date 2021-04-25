#include <iostream>
#include <cstring>
using namespace std;
struct elem
{
    int inf;
    elem* pun;
};
typedef elem* lista;
int head(lista p){return p->inf;}
lista tail(lista p){return (p->pun);}
bool empty(lista l)
{
    if(l == NULL) return true;
    return false;
}
void stampa_lista(lista p)
{
	if(p == NULL)
		cout<<"La lista è vuota."<<endl;
    while(p != NULL)
     {
        cout<<head(p)<<" "<<p<<endl;
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
        elem* p = new elem;
        cout<<"Inserire elemento: ";
        cin>>p->inf;
        testa = insert_elem(testa ,p);
    }
    return testa;
}
lista delete_elem(lista l , elem* e)
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
void salta(lista testa , int k) // 13 12 11 10 9 8 7 6 5 4 3 2 1 non funzionante , ancora da debuggare
{
	// testa tiene traccia del primo elemento.
	lista appoggio;
	lista da_cancellare;
	if(testa != NULL)
	{
		cout<<testa->inf<<" "<<testa<<endl;
		testa = delete_elem(testa , testa);
	}
	appoggio = testa;
	while(testa != NULL)
	{
		for(int i = 0 ; i < k-1 ; i++)
		{
			appoggio = tail(appoggio);
			if(appoggio == NULL)
				appoggio = testa;
		}
		da_cancellare = appoggio; // elemento su cui sono arrivato.
		cout<<da_cancellare->inf<<" "<<da_cancellare<<endl;
		appoggio = tail(appoggio);
		if(appoggio == NULL)
			appoggio = testa;
		testa  = delete_elem(testa ,da_cancellare);
	}
	cout<<endl;
}
lista cancella_pari(lista testa)
{
	lista p = testa;
	lista da_cancellare; // variabile d'appoggio per cancellare p
	if(testa == NULL)
		return NULL;
	while(p != NULL)
	{
		if((p->inf)%2 == 0)
		{
			da_cancellare = p;
            p = tail(p);
			testa = delete_elem(testa,da_cancellare);
		}
        else
            p = tail(p);
	}
	cout<<endl;
	return testa;
}
int main()
{
	lista testa;
	while(true)
	{
		cout<<"1) Crea lista."<<endl;
		cout<<"2) Stampa lista."<<endl;
		cout<<"3) Salti."<<endl;
		cout<<"4) Delete first elem."<<endl;
		cout<<"5) Cancella pari."<<endl;
		cout<<"6) Delete elem."<<endl;
		int scelta;
		cout<<">> ";
		cin>>scelta;
		switch(scelta)
		{
		case 1:
			int n;
			cout<<"Inserire numero elementi: ";
			cin>>n;
			testa = crea_lista(n);
			break;
		case 2:
			stampa_lista(testa);
			cout<<endl;
			break;
		case 3:
			salta(testa, 3);
			break;
		case 4:
			testa = delete_elem(testa , testa);
			break;
		case 5:
			testa = cancella_pari(testa);
			break;
		case 6:
			testa = delete_elem(testa , tail(tail(testa)));
			break;
		default:
			cout<<"Programma terminato."<<endl;
			break;
		}
	}
	return 0;
}
