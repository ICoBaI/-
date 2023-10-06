## Информация о проекте
Необходимо организовать систему учета для питомника, в котором живут
домашние и вьючные животные.

## Задание
1. Используя команду cat в терминале операционной системы Linux, создать
два файла Домашние животные (заполнив файл собаками, кошками,
хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и
ослы), а затем объединить их. Просмотреть содержимое созданного файла.
Переименовать файл, дав ему новое имя (Друзья человека).

![Task 1](https://i.imgur.com/QBtrCKQ.png)

2. Создать директорию, переместить файл туда.

![Task 2](https://i.imgur.com/8uyp8qM.png)

3. Подключить дополнительный репозиторий MySQL. Установить любой пакет
из этого репозитория.

![Task 3](https://i.imgur.com/Lj3fSIx.png)

![Task 3](https://i.imgur.com/1G6LP68.png)

![Task 3](https://i.imgur.com/DLDE8Nl.png)

4. Установить и удалить deb-пакет с помощью dpkg.

![Task 4](https://i.imgur.com/42jb2xc.png)

5. Выложить историю команд в терминале ubuntu

![Task 5](https://i.imgur.com/VePa1il.png)

6. Нарисовать диаграмму, в которой есть класс родительский класс, домашние
животные и вьючные животные, в составы которых в случае домашних
животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные
войдут: Лошади, верблюды и ослы).

![Task 6](https://i.imgur.com/2UsTghE.png)

7. В подключенном MySQL репозитории создать базу данных “Друзья
человека”

```sql
CREATE DATABASE Human_friends;
```

8. Создать таблицы с иерархией из диаграммы в БД

```sql
USE Human_friends;
CREATE TABLE animal_classes
(
	Id INT AUTO_INCREMENT PRIMARY KEY, 
	Class VARCHAR(20)
);

INSERT INTO animal_classes (Class)
VALUES ('вьючные'),
('домашние');  


CREATE TABLE packed_animals
(
	  Id INT AUTO_INCREMENT PRIMARY KEY,
    Genus VARCHAR (20),
    Class_id INT,
    FOREIGN KEY (Class_id) REFERENCES animal_classes (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO packed_animals (Genus, Class_id)
VALUES ('Верблюды', 1),
('Ослы', 1),  
('Лошади', 1); 
    
CREATE TABLE home_animals
(
	  Id INT AUTO_INCREMENT PRIMARY KEY,
    Genus VARCHAR (20),
    Class_id INT,
    FOREIGN KEY (Class_id) REFERENCES animal_classes (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO home_animals (Genus, Class_id)
VALUES ('Кошки', 2),
('Хомяки', 2),  
('Собаки', 2);
```
9. Заполнить низкоуровневые таблицы именами(животных), командами
которые они выполняют и датами рождения

```sql
CREATE TABLE dogs 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20), 
    Commands VARCHAR(50),
    Birthday DATE,
    Genus int,
    Foreign KEY (Genus) REFERENCES home_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO dogs (Name, Commands, Birthday, Genus)
VALUES ('Хок', 'лапу, голос', '2009-08-10', 1);

CREATE TABLE hamsters 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20), 
    Commands VARCHAR(50),
    Birthday DATE,
    Genus int,
    Foreign KEY (Genus) REFERENCES home_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO hamsters (Name, Commands, Birthday, Genus)
VALUES ('Шар', 'спать','2013-10-12', 2);

CREATE TABLE cats 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20), 
    Commands VARCHAR(50),
    Birthday DATE,
    Genus int,
    Foreign KEY (Genus) REFERENCES home_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO cats (Name, Commands, Birthday, Genus)
VALUES ('Пром', 'кс-кс-кс', '2022-02-02', 3);

CREATE TABLE horses 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20), 
    Commands VARCHAR(50),
    Birthday DATE,
    Genus int,
    Foreign KEY (Genus) REFERENCES packed_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO horses (Name, Commands, Birthday, Genus)
VALUES ('Молния', 'бегом, шагом', '2013-12-12', 1);

CREATE TABLE donkeys 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20), 
    Commands VARCHAR(50),
    Birthday DATE,
    Genus int,
    Foreign KEY (Genus) REFERENCES packed_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO donkeys (Name, Commands, Birthday, Genus)
VALUES ('Сахарок', NULL,'2019-04-10', 2);

CREATE TABLE camels 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20), 
    Commands VARCHAR(50),
    Birthday DATE,
    Genus int,
    Foreign KEY (Genus) REFERENCES packed_animals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO camels (Name, Commands, Birthday, Genus)
VALUES ('Пусан', 'лечь', '2011-11-11', 3);
```

10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой
питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу.

```sql
DELETE FROM camels;

SELECT Name, Commands, Birthday, Genus
FROM horses
UNION
SELECT Name, Commands, Birthday, Genus
FROM donkeys
```
11. Создать новую таблицу “молодые животные” в которую попадут все
животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
до месяца подсчитать возраст животных в новой таблице

```sql
CREATE TEMPORARY TABLE animals AS 
SELECT *, 'Лошади' AS genus_id FROM horses
UNION SELECT *, 'Ослы' AS genus_id FROM donkeys
UNION SELECT *, 'Собаки' AS genus_id FROM dogs
UNION SELECT *, 'Кошки' AS genus_id FROM cats
UNION SELECT *, 'Хомяки' AS genus_id FROM hamsters;

CREATE TABLE yang_animal AS
SELECT Name, Birthday, Commands, genus_id, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) AS Age_in_month
FROM animals WHERE Birthday BETWEEN ADDDATE(curdate(), INTERVAL -3 YEAR) AND ADDDATE(CURDATE(), INTERVAL -1 YEAR);
```
12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
прошлую принадлежность к старым таблицам.

```sql
SELECT h.Name, h.Birthday, h.Commands, pa.Genus, ya.Age_in_month 
FROM horses h
LEFT JOIN yang_animal ya ON ya.Name = h.Name
LEFT JOIN packed_animals pa ON pa.Id = h.Genus
UNION 
SELECT d.Name, d.Birthday, d.Commands, pa.Genus, ya.Age_in_month 
FROM donkeys d 
LEFT JOIN yang_animal ya ON ya.Name = d.Name
LEFT JOIN packed_animals pa ON pa.Id = d.Genus
UNION
SELECT c.Name, c.Birthday, c.Commands, ha.Genus, ya.Age_in_month 
FROM cats c
LEFT JOIN yang_animal ya ON ya.Name = c.Name
LEFT JOIN home_animals ha ON ha.Id = c.Genus
UNION
SELECT d.Name, d.Birthday, d.Commands, ha.Genus, ya.Age_in_month 
FROM dogs d
LEFT JOIN yang_animal ya ON ya.Name = d.Name
LEFT JOIN home_animals ha ON ha.Id = d.Genus
UNION
SELECT hm.Name, hm.Birthday, hm.Commands, ha.Genus, ya.Age_in_month 
FROM hamsters hm
LEFT JOIN yang_animal ya ON ya.Name = hm.Name
LEFT JOIN home_animals ha ON ha.Id = hm.Genus;
```
