// ���� GetPut.cpp � ��������� ����� � ������
#include<iostream>
using namespace std;

void Get(float& a, float& b, float& h1, float& c, float& d, float& h2)
{
	setlocale(LC_ALL, "rus");
	cout << "������� ������ ������� ������� ��������� X: ";
	cin >> a;
	cout << "������� ������� ������� ������� ��������� X: ";
	cin >> b;
	cout << "������� ��� ��������� X: ";
	cin >> h1;
	cout << "������� ������ ������� ������� ��������� Y: ";
	cin >> c;
	cout << "������� ������� ������� ������� ��������� Y: ";
	cin >> d;
	cout << "������� ��� ��������� Y: ";
	cin >> h2;
}

void Put(int nPos)
{
	setlocale(LC_ALL, "rus");
	cout << "���������� ������������� �������� �������: " << nPos << endl;
}
