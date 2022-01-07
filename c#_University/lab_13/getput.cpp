
// файл GetPut.cpp с функци€ми ввода и вывода
#include<iostream>
using namespace std;
void Get(float& a, float& b, float& h)
{
	setlocale(LC_ALL, "rus");
	cout << "¬ведите нижнюю границу отрезка: ";
	cin >> a;
	cout << "¬ведите верхнюю границу отрезка: ";
	cin >> b;
	cout << "¬ведите шаг таблицы: ";
	cin >> h;
}
void Put(float z)
{
	setlocale(LC_ALL, "rus");
	cout << endl << "произведение значений функции y=f(x) при y>0  " << z << endl;
	
}
