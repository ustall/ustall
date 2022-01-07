// פאיכ Main.cpp
#include<iostream>

void Get(float& a, float& b, float& h1, float& c, float& d, float& h2);
void Put(int nPos);
void RegCikl2(float a, float b, float h1, float c, float d, float h2, int&nPos);

void main()
{
	float a, b, h1, c, d, h2, sPos;
	int nPos;
	Get(a, b, h1, c, d, h2);
	RegCikl2(a, b, h1, c, d, h2, nPos);
	Put(nPos);
	system("PAUSE");
}
