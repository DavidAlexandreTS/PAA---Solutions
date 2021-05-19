#include<iostream>
#include<climits>

using namespace std;

int soma_max(int seq[], int size)
{
	int maxm = INT_MIN, max_end = 0;

	for (int i = 0; i < size; i++)
	{
		max_end = max_end + seq[i];
		if (maxm < max_end)
			maxm = max_end;

		if (max_end < 0)
			max_end = 0;
	}
	return maxm;
}

int main()
{
	int seq[] = {5, 15, -30, 10, -5, 40, 10};
	int n = sizeof(seq)/sizeof(seq[0]);
	int max_sum = soma_max(seq, n);
	cout << "A soma Máxima é " << max_sum;
	return 0;
}
