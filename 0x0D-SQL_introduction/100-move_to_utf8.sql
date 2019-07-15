-- converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET UTF8 COLLATE utf8mb4_unicode_ci;
ALTER TABLE second_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE second_table change name nameVARCHAR(256) CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_\
 ci;
