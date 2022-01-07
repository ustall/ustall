// פאיכ main.cpp
#include<iostream>

void Get(float& a, float& b, float& h);
void Put(float z);
void RegCikl(float a, float b, float h, float& z);

void main()
{
	float a, b, h, z;
	int nPos, nNeg;
	Get(a, b, h);
	RegCikl(a, b, h, z);
	Put(z);
	system("PAUSE");
}
