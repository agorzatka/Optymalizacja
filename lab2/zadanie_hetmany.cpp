#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
int ilosc_hetmanow(vector <int> p, int w){
	int ih=0;
	int n = sqrt(p.size());
	if(w>=n){
		for(int i=0;i<p.size();i++) if(p[i] == 1) ih++;
		return ih;
	}
	for(int i=0;i<n;i++){
		//cout<<"w: "<<w<<" i::"<<i<<endl;
		if(p[w * n + i] == 0){
			vector <int> p1 = p;
			p1[w*n+i] = 1;
			//wypelnianie kolumny
			for(int j = w + 1; j < n; j++) p1[ j * n + i] = -1;
			//wypelnianie przkątej rosnącej
			int wd = w + 1;
			for(int j = i-1; j >= 0 && wd < n; j--){
				p1[wd * n + j] = -1;
				wd++;
			}
			//wypelnienie przekatnej malejacej
			wd = w+1;
			for(int j = i+1; j < n && wd < n; j++){
                                p1[wd * n + j] = -1;
                                wd++;
                        }
			/*
			for(int j=0;j<n;j++){
				for(int q=0;q<n;q++){
					cout<<p1[j*n+q]<<" ";
				}
				cout<<"\n";
			}*/
			int ih1 = ilosc_hetmanow(p1, w+1);
			if(ih1 > ih) ih = ih1;
		}
	}
	if(ih==0){
		int ih1 = ilosc_hetmanow(p,w+1);
		if(ih1 > ih) ih = ih1;
	}
	return ih;
}
int main(){
	int n;
	cin>>n;
	vector <int> p;
	for(int i=0;i<n*n;i++) p.push_back(0);
	cout<<ilosc_hetmanow(p,0)<<endl;
}
