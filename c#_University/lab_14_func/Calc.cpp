// файл Calc.cpp
#include<iostream>
using namespace std;

float f(float x, float y);

void RegCikl2(float a, float b, float h1, float c, float d, float h2, int&nPos)
{
	setlocale(LC_ALL, "rus");
	int n1 = int((b - a) / h1) + 1;
	int n2 = int((d - c) / h2) + 1;

	nPos = 0;
	float x, y, z;
	cout << endl << "Таблица значений функции" << endl;
	cout << "\tx\ty\tz" << endl;
	x = a;
	for (int i = 1; i <= n1; i++)
	{
		y = c;
		for (int j = 1; j <= n2; j++)
		{
			z = f(x, y);
			if (z > 0) { nPos++; }
			cout << "\t" << x << "\t" << y << "\t" << z << endl;
			y += h2;
		}
		x += h1;
	}

}

float f(float x, float y)
{
	if (x >= -2 && x <= 2 && y >= -1 && y <= 1)
	{
		return(pow(2.71828, x) + y);
		
	}
	else
	{
		return (x > -3 && x < -2 && y>-2 && y < -1) ? (x+y+4) : (0);
	}
}
