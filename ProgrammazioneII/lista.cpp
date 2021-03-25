#include <iostream>
using namespace std;
struct elem
{
    int inf;
    elem* pun;
};
typedef elem * lista;
int head(lista p){return p->inf;}
lista tail(lista p){return (p->pun);}
void stampa_lista(lista p)
{
    while(p!= NULL)
     {
        cout<<head(p)<<" ";
        p = tail(p);
     }
     cout<<endl;
}
int main()
{
    lista testa = new elem;
    testa ->inf = 3;
    elem *p = new elem;
    p->inf = 7;
    p->pun = NULL;
    testa->pun = p;
    stampa_lista(testa);
return 0;
}
