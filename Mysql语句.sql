-- 创建数据库
CREATE TABLE IF NOT EXISTS 'db_name' DEFAULT CHARACTER SET 'UTF-8';

USE 'tbl_name';

-- 创建用户表
-- id, username, age, sex, email, addr, birth, salary, tel, married
-- 当需要输入中文的时候，需要临时转换客户端的编码方式
-- SET NAMES GBK; \s查询
-- 字段注释通过COMMENT
CREATE TABLE IF NOT EXISTS 'user'(
	id SMALLINT,
	username VARCHAR(20),
	age TINYINT,
	sex ENUM('男'，'女'，'保密')
	email VARCHAR(50),
	addr VARCHAR(200),
	birth YEAR,
	salary FLOAT(8,2),
	tel INT,
	married TINYINT(1)  COMMENT '0代表未结婚 非0代表已结婚'
)ENGINE=INNODB CHARSET=UTF8;


-- 创建课程表 
-- cid, courseName, courseDesc
CREATE TABLE IF NOT EXISTS 'course'(
	cid TINYINT,
	courseName VARCHAR(50),
	courseDesc VARCHAR(200)
)ENGINE=INNODB CHARACTER=UTF8;

SELECT id,username,age,age BETWEEN 10 AND 30 FROM cms_user;
SELECT id,username,age,age IN(21,31,41,51) FROM cms_user;
SELECT s LIKE '_';
SELECT id, username, username LIKE '____' FROM cms_user;
SELECT id, username username REGEXP '^t' FROM cms_user;
-- 数据检索效率 CHAR>VARCHAR>TEXT
-- 查询表结构 DESC tbl_name
-- 集合
CREATE TABLE IF NOT EXISTS test8(
	fav SET('A', 'B', 'C', 'D')
);
-- 插入时间
CREATE TABLE IF NOT EXISTS test(
	test TIME
);
INSERT test10 VALUES('1 12:12:12');
-- 完整性约束
CREATE TABLE IF NOT EXISTS user1(
	id INT PRIMARY KEY,
	username VARCHAR(20)
);
-- 查看创建表的定义
SHOW CREATE TABLE user1;
INSERT user1 VALUES(1,'ABC')
-- 复合主键
CREATE TABLE IF NOT EXISTS user2(
	id INT,
	username VARCHAR(20)，
	card CHAR(18),
	PRIMARY KEY(id, card)
);
-- 自增长
CREATE TABLE IF NOT EXISTS user2(
	id SMALLINT KEY AUTO_INCREMENT,
	username VARCHAR(20)，
	card CHAR(18)
);
-- 测试NOT NULL
CREATE TABLE IF NOT EXISTS user7(
	id INT UNSIGNED KEY AUTO_INCREMENT,
	USERNAME VARCHAR(20) NOT NULL,
	passward CHAR(20) NOT NULL,
	age TINYINT UNSIGNED DEFAULT 18,
	addr VARCHAR(50) NOT NULL DEFAULT '北京',
	sex ENUM('男'，'女'，'保密') NOT NULL DEFAULT '男'
); 
CREATE TABLE IF NOT EXISTS user9(
	id TINYINT UNSIGNED KEY AUTO_INCREMENT,
	username VARCHAR(20) NOT null UNIQUE,
	card CHAR(18) UNIQUE
);

CREATE TABLE [IF NOT EXISTS] tbl_name(
字段名称 字段类型 [UNSIGNED | ZEROFILL] [NOT NULL] [DEFAULT 默认值] [[PRIMARY] KEY | UNIQUE [KEY]] [AUTO_INCREMENT]
)ENGINE=INNODB CHARSET=UTF8 AUTO_INCREMENT=100;

 -- 将user10重命名成user11
 ALTER TABLE user10 RENAME [TO | AS | ] user11;
RENAME TABLE user10 TO user11;

--字段
ALTER TABLE tbl_name ADD 字段名称 字段类型 [完整性约束条件] [FRIST | AFTER 字段名称]
ALTER TABLE tbl_name DROP 字段名称 
ALTER TABLE tb_name MODIFY 字段名称 字段类型 [完整性约束条件] [FRIST | AFTER]
ALTER TABLE tbl_name CHANGE 旧字段名称 新字段名称 字段类型 [完整性约束条件] [FRIST | AFTER 字段名称]
-- 默认值
ALTER TABLE tbl_name ALTER 字段名称 SET DEFAULT 默认值
ALTER TABLE tbl_name ALTER 字段名称 DROP DEFAULT
-- 主键
ALTER TABLE tbl_name ADD [CONSTRAINT [symbol]] PRIMARY KEY[index_type](字段名称,...)
ALTER TABLE tbl_name DROP PRIMARY KEY
-- 唯一
ALTER TABLE tbl_name ADD [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY][索引名称](字段名称,...)
ALTER TABLE tbl_name DROP {INDEX | KEY} index_name
-- 存储引擎
ALTER TABLE tbl_name ENGINE=存储引擎名称
-- 设置自增长的值 
ALTER TABLE tbl_name AUTO_INCREMENT=值

-- 表
DROP TABLE [IF EXISTS] tbl_name[,tbl_name]

-- 数据
INSERT [INTO] tbl_name VALUES|VALUE(值...)
INSERT [INTO] tbl_name(字段名称1,...) VALUES|VALUE(值1,...)
INSERT [INTO] tbl_name[(字段名称...)] VALUES(值...),(值...)...
INSERT [INTO] tbl_name SET 字段名称=值,...
INSERT [INTO] tbl_name[(字段名称,...)] SELECT 字段名称 FROM tbl_name [WHERE 条件]
UPDATE tbl_name SET 字段名称=值,... [WHERE 条件][ORDER BY 字段名称][LIMIT 限制条数]
DELETE FROM tbl_name [WHERE 条件][ORDER BY 字段名称][LIMIT 限制条数]
TRUNCATE [TABLE] tbl_name

-- 查询
SELECT select_expr[, select_expr]
[
	FROM table_referrnces
	[WHERE 条件]
	[GROUP BY {col_name | position} [ASC | DESC], ... 分组]
	[HAVING 条件 对分组结果进行二次筛选]
	[ORDER BY {col_name | position} [ASC | DESC], ...排序]
	[LIMIT 限制显示条数]
]
-- 检测字段为NULL 需用<=>NULL
-- 检测字段是否为空 字段名称 IS NULL
-- 查询忽略大小写
SELECT * FROM cms_user WHERE username IN('abc', '123','sdd');

-- 模糊查询
-- %:代表0个或者多个任意字符
-- _:代表1个任意字符
SELECT * FROM cms_user WHERE username LIKE 'abc'

-- 分组查询 GROUP BY
SELECT * FROM cms_user GROUP BY id，username;

-- 得到分组详情
SELECT GROUP_CONCAT(字段名称) FROM tbl_name GROUP BY 字段名称

-- COUNT(字段名称) 如果字段中包含NULL 则不统计在内
-- HAVING子句对分组结果进行二次筛选
SELECT sex, GROUP_CONCAT(username) AS users,
COUNT(*) AS totalUsers,
MAX(age) AS max_age,
SUM(age) AS sum_age,
FROM cms_user
WHERE id>=2
GROUP BY sex
HAVING COUNT(*)>2 AND MAX(age)>60;

--按照id降序排列DESC 默认的是ASC
SELECT * FROM cms_user ORDER BY age ASC, id DESC;

-- 内连接查询 JOIN | CROSS JOIN | INNER JOIN 通过ON连接条件
SELECT u.id, u.username, u.email, u.sex, p.proName
FROM cms_user AS u
INNER JOIN provinces AS P
ON u.proId=p.id;

-- 外键保证数据的一致性，完整性
-- 外键列必须存在索引
-- 存储引擎只能为INNODB
-- 参照列和外键列必须具有相似的数据类型
CONSTRAINT 外键名称 FOREIGN KEY(字段名称) REFERENCES tbl_name(字段名称1)
ALTER TABLE tbl_name DROP FOREIGN KEY 外键名称
ALTER TABLE tbl_name ADD CONSTRAINT 外键名称 FOREIGN KEY(字段名称) REFERENCES tbl_name1(字段名称1)

-- 级联
FOREIGN KEY(字段名称) REFERENCES tbl_name(字段名称1) ON DELETE CASCADE ON UPDATE CASCADE

-- 联合查询
-- UNION 会去重 UNION ALL 不会去重

-- 子查询 [NOT] IN
SELECT id, username FROM employee WHERE depId IN(SELECT id FROM department);

-- 正则表达式匹配
SELECT * FROM cms_user WHERE username REGEXP '^t';