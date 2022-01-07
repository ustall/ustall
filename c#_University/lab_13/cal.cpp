// файл Calc.cpp
#include<iostream>
#include<cmath>
using namespace std;
float func(float x);
void RegCikl(float a, float b, float h, float&z)
{
	setlocale(LC_ALL, "rus");
	int n = floor((b - a) / h) + 1;
	float x, y;
	z = 1;
	cout << endl << "Таблица значений функции" << endl;
	cout << "\tx\ty" << endl;
	for (int i = 1; i <= n; i++)
	{
		x = a + (i - 1)*h;
		y = func(x);
		if (y>0) z=z*y;
		cout << "\t" << x << "\t" << y << endl;
	}
	if (z == 1)
	{
		z = 0;
	}
}

float func(float x)
{
	double y = pow(x, 4) + pow(x, 3) - 10 * x - 34 * x - 25;
	return y;
}
