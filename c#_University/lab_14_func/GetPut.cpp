// файл GetPut.cpp с функциями ввода и вывода
#include<iostream>
using namespace std;

void Get(float& a, float& b, float& h1, float& c, float& d, float& h2)
{
	setlocale(LC_ALL, "rus");
	cout << "Введите нижнюю границу отрезка изменения X: ";
	cin >> a;
	cout << "Введите верхнюю границу отрезка изменения X: ";
	cin >> b;
	cout << "Введите шаг изменения X: ";
	cin >> h1;
	cout << "Введите нижнюю границу отрезка изменения Y: ";
	cin >> c;
	cout << "Введите верхнюю границу отрезка изменения Y: ";
	cin >> d;
	cout << "Введите шаг изменения Y: ";
	cin >> h2;
}

void Put(int nPos)
{
	setlocale(LC_ALL, "rus");
	cout << "Количество положительных значений функции: " << nPos << endl;
}
