
// ���� GetPut.cpp � ��������� ����� � ������
#include<iostream>
using namespace std;
void Get(float& a, float& b, float& h)
{
	setlocale(LC_ALL, "rus");
	cout << "������� ������ ������� �������: ";
	cin >> a;
	cout << "������� ������� ������� �������: ";
	cin >> b;
	cout << "������� ��� �������: ";
	cin >> h;
}
void Put(float z)
{
	setlocale(LC_ALL, "rus");
	cout << endl << "������������ �������� ������� y=f(x) ��� y>0  " << z << endl;
	
}
