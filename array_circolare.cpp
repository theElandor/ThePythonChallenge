#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <stdlib.h>
#include <windows.h>
#include <unistd.h>
using namespace std;
void d(int arr[], int ll){
    for(int i = 0 ; i < ll ; i++){
        if(arr[i]>=0)
            cout<<arr[i]<<" ";
    }
}
int inserisci_fine(int arr[], int DIM ,int val,int i_fine){
    int in_fine = i_fine; //creo una copia del parametro per non causare problemi
    in_fine = (in_fine+1)%DIM;
    arr[in_fine] = val;
    return in_fine;
}
void inizializza(int arr[], int ll){
    for(int i = 0 ; i < ll ; i++){  
        arr[i] = 0;
    }
}
int inserisci_inizio(int arr[], int DIM ,int val,int i_inizio){
    int in_inizio = i_inizio; //creo una copia del parametro per non causare problemi
    in_inizio = in_inizio-1;
    if(in_inizio<0)
        in_inizio = DIM-1;
    arr[in_inizio]=val; 
    return in_inizio;

}
int main(){
    int DIM = 10;
    int elementi = 0;
    int arr[DIM];
    int scelta;
    int val;
    inizializza(arr,DIM);
    int inizio = (DIM/2)+1, fine = inizio-1;
    cout<<"---------MENU----------"<<endl;
    cout<<"1 : inserisci alla fine ;"<<endl;
    cout<<"2 : inserisci all'inizio ;"<<endl;
    cout<<"3 : stampa array ;"<<endl;
    cout<<"-----------------------"<<endl;
    while(true){
    cout<<endl<<">> ";
    cin>>scelta;
    switch(scelta){
        case 1:
            if(elementi == DIM){
                cout<<"Array pieno."<<endl;
                break;
            }
            cout<<"Inserire valore: ";
            cin>>val;
            fine = inserisci_fine(arr,DIM,val,fine);
            elementi++;
            break;
        case 2:
            if(elementi == DIM){
                cout<<"Array pieno."<<endl;
                break;
            }
            cout<<"Inserire valore: ";
            cin>>val;
            inizio = inserisci_inizio(arr,DIM,val,inizio);
            elementi++;
            break;
        case 3:
            d(arr,DIM);
            break;
        default:
            cout<<"Scelta non valida."<<endl;
            break;
    }
    }
    return 0;
}