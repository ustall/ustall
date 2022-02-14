create table PoliceStation(ID int not null primary key, 
                           Address nchar(100) not null, 
						   NameOfStation nchar(100) not null);

create table Evidence(ID int not null primary key,
						ID_PoliceStation int not null,
						FOREIGN KEY (ID_PoliceStation) REFERENCES PoliceStation(Id)on delete cascade,
						EvidenceName nchar(70) not null);

create table Detective(ID int not null primary key,
						ID_PoliceStation int not null,
						FOREIGN KEY (ID_PoliceStation) REFERENCES PoliceStation(Id)on delete cascade,
						FullName nchar(70) not null,
						Rank nchar(70) not null);
						
create table CourtCase(Id int not null primary key,
					   Id_Detective int not null,
					   FOREIGN KEY (Id_Detective) REFERENCES Detective(Id)on delete cascade,
					   NameOfCase nchar(70) not null,
				       StatusOFCase nchar(50) not null);

create table Suspect(Id int not null primary key,
					   Id_CourtCase int not null,
					   FOREIGN KEY (Id_CourtCase) REFERENCES CourtCase(Id)on delete cascade,
					   FullName nchar(70) not null,
					   Address nchar(100) not null,
				       PhoneNumber nchar(20) not null);

create table Witness(Id int not null primary key,
					   Id_CourtCase int not null,
					   FOREIGN KEY (Id_CourtCase) REFERENCES CourtCase(Id)on delete cascade,
					   FullName nchar(70) not null,
					   Address nchar(100) not null,
				       PhoneNumber nchar(20) not null);

create table Wictim(Id int not null primary key,
					   Id_CourtCase int not null,
					   FOREIGN KEY (Id_CourtCase) REFERENCES CourtCase(Id)on delete cascade,
					   FullName nchar(70) not null,
					   Address nchar(100) not null,
				       PhoneNumber nchar(20) not null);

create table CrimeScene(Id int not null primary key,
					   Id_CourtCase int not null,
					   FOREIGN KEY (Id_CourtCase) REFERENCES CourtCase(Id)on delete cascade,
					   Address nchar(100) not null,
				       TimeOfCrime nchar(50) not null);
						
						
				  
insert into PoliceStation(ID, Address ,NameOfStation)
values
(1,'Street "Molodegnay" Home 25' ,'OVD "Molodegnay"'),
(2,'Street "Stoiteley" Home 34' ,'OVD "Stroiteley"'),
(3,'Street "Udaltsova" Home 72' ,'OVD "Udaltsova"');


insert into Evidence(ID ,ID_PoliceStation,
					   EvidenceName)
values
(1,(select ID from PoliceStation where ID=1 ), 'A1'),
(2,(select ID from PoliceStation where ID=2 ), 'B3'),
(3,(select ID from PoliceStation where ID=3 ), 'C7');

insert into Detective(ID ,ID_PoliceStation,
					   FullName, Rank)
values
(1,(select ID from PoliceStation where ID=1 ), 'Anatoly Belyev', 'Major'),
(2,(select ID from PoliceStation where ID=2 ), 'Vladimir Ivanov', 'Lieutenant'),
(3,(select ID from PoliceStation where ID=3 ), 'Sergey Petrov', 'Major');

insert into CourtCase(ID ,Id_Detective,
					   NameOfCase, StatusOFCase)
values
(1,(select ID from Detective where ID=1 ), 'The roobery case','Administrative'),
(2,(select ID from Detective where ID=2 ), 'The murder case','Criminal'),
(3,(select ID from Detective where ID=3 ), 'The scam case', 'Administrative');

insert into Suspect(ID ,Id_CourtCase,
					   FullName, Address, PhoneNumber)
values
(1,(select ID from CourtCase where ID=1 ), 'Radion Rascolnikov', 'Street "Molodegnay" Home 26', '+7 111 1111 11 11'),
(2,(select ID from CourtCase where ID=2 ), 'Dmitry Nikolaev', 'Street "Stoiteley" Home 35','+7 111 1111 11 12'),
(3,(select ID from CourtCase where ID=3 ), 'Victor Rebrov', 'Street "Udaltsova" Home 73','+7 111 1111 11 13');

insert into Witness(ID ,Id_CourtCase,
					   FullName, Address, PhoneNumber)
values
(1,(select ID from CourtCase where ID=1 ), 'Arseny Krugly', 'Street "Molodegnay" Home 27', '+7 111 1111 11 14'),
(2,(select ID from CourtCase where ID=2 ), 'Aleksandr Aleksandrov', 'Street "Stoiteley" Home 36','+7 111 1111 11 15'),
(3,(select ID from CourtCase where ID=3 ), 'Svetlana Ustugova', 'Street "Udaltsova" Home 74','+7 111 1111 11 16');

insert into Wictim(ID ,Id_CourtCase,
					   FullName, Address, PhoneNumber)
values
(1,(select ID from CourtCase where ID=1 ), 'Maxim Serov', 'Street "Molodegnay" Home 28', '+7 111 1111 11 17'),
(2,(select ID from CourtCase where ID=2 ), 'Roman Avdeev', 'Street "Stoiteley" Home 37','+7 111 1111 11 18'),
(3,(select ID from CourtCase where ID=3 ),'Anna Lilova', 'Street "Udaltsova" Home 75','+7 111 1111 11 19');

insert into CrimeScene(ID ,Id_CourtCase,
					   Address, TimeOfCrime)
values
(1,(select ID from CourtCase where ID=1 ),'Street "Molodegnay" Home 29', '29.04.2012 14:00'),
(2,(select ID from CourtCase where ID=2 ),'Street "Stoiteley" Home 38','14.05.2015 16:58'),
(3,(select ID from CourtCase where ID=3 ),'Street "Udaltsova" Home 76','01.12.20120 13:45');


