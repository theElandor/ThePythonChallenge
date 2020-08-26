#include <bits/stdc++.h>
using namespace std;
// looking for sBBBsBBBs
bool look_for_3B(string text , int i){
	bool found = false;
	for(int k= 0 ; k < 3;k++){
		if (islower(text[k])==true)
			found = true;
	}
	if(found == false)
	return (true);
	else
	return(false);
	
}
int main(){
string text = "sBBBsBBBsKKKKKKKKK";
cout<<text<<endl;
for(int i = 0 ; i < text.length();i++){
	if(islower(text[i])){
		if(look_for_3B(text , i+1) == true){
			if(islower(text[i+4])){
				if(look_for_3B(text,i+5)== true){
					if(islower(text[i+8])){
						for(int j = i ; j < 8;j++){
							cout<<text[j];
						}
					}
				}
			}
		}
	
}
}
return 0;
}
