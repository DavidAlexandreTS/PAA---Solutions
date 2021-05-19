
#include <bits/stdc++.h>
using namespace std;

int Sumpt(vector<vector<int> >& Array)
{
	int tt[Array.size()];
	int n = Array.size() - 1;

	for(int i = 0; i < Array[n].size(); i++)
		tt[i] = Array[n][i];

	for(int i = A.size() - 2; i >= 0; i--)
	{
		for(int j = 0; j < Array[i].size(); j++)
			tt[j] = Array[i][j] + min(tt[j], tt[j + 1]);
		
	}

	return tt[0];
}

int main()
{
	vector<vector<int> > Array{ { 4 }, { 6, 18 }, { 3, 9, 13 } };
	cout << Sumpt(Array);
	return 0;
}
