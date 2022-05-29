SQL基础语法&运行原理


【SQL查询语句语法结构和运行顺序】
    语法结构：select--from--where--group by--having--order by--limit
    运行顺序：from--where--group by--having--order by--limit--select


【基础语法和运行原理】
    【基础语句】
        主知识点一：select&from
            【知识点引入】
                【标准语法】
                    select 字段名
                    from 表名

                【语法解释】
                    select 字段名 决定这一段查询最后展示的字段
                    from 表名 指定这段查询语句涉及的数据来源

                这是一段查询语句中必不可少的两个核心语句，select和from分别是两个核心语句中的关键字

            【总结】
                基础语法
                    select  字段名
                    from  表名

                别名语法
                    select  字段名 as 别名
                    from  表名
                    注意：as可以省略

                查询多列
                    select   字段名1,字段名2,字段名3
                    from  表名

                查询所有列
                    select *
                    from  表名

                数据去重
                    select  distinct  字段名
                    from 表名

                select中的计算字段
                    select   字段名,计算字段
                    from  表名称
                    注意：计算字段中的算式所涉及的字段必须是表格中包含的，或者算式本身可以独立运算



        主知识点二：where
            【知识点引入】
                【标准语法】
                    select 字段名
                    from 表名
                    [where 表达式]

                【语法解释】
                    where 表达式 限定查询行必须满足的条件
                    where核心子句是可选项，使用该子句是为了通过表达式筛选出符合查询条件的行数据


            【总结】
                标准语法
                    select 字段名
                    from 表名
                    where 表达式

                运算符查询语法
                    select 字段名
                    from 表名
                    where 字段名 运算符 值

                模糊查询语法
                    select 字段名
                    from 表名
                    where 字段名 like '通配符+字符'

                使用多条件查询
                    select 字段名
                    from 表名
                    where 条件代码1 and|or 条件代码2

                运算符

                通配符



        主知识点三：order by
            【知识点引入】
                【标准语法】
                    select 字段名
                    from 表名
                    [where 表达式]
                    [order by 字段名 asc|desc]

                【语法解释】
                    order by 字段名 asc|desc  规定查询出的结果集显示的顺序
                    order by核心子句是可选项，使用该子句是为了对被查询出的结果集，指定依据字段排序
                    asc指定该字段升序排序，desc为降序排序，不写则默认为升序排序


            【总结】
                【标准语法】
                    select 字段名1
                    from 表名
                    [where 表达式]
                    [order by 字段名 asc|desc]



        主知识点四：limit
            【知识点引入】
                【标准语法】
                    select 字段名
                    from 表名
                    [where 表达式]
                    [order by 字段名 asc|desc]
                    [limit [位置偏移量,]行数]

                【语法解释】
                    limit [位置偏移量,]行数 限制查询结果集显示的行数
                    limit子句是可选项，行数是子句中的必选参数，参数位置偏移量是可选参数


            【总结】
                【查询结果返回前n行】
                    select 字段名
                    from 表名
                    [where 表达式]
                    [order by 字段名 asc|desc]
                    [limit n]

                【查询结果返回第x+1行开始的n行到x+n行】
                    select 字段名
                    from 表名
                    [where 表达式]
                    [order by 字段名 asc|desc]
                    [limit x,n]



        主知识点五：聚合函数&group by
            【知识点引入】
                聚合函数
                    聚合函数适用于需要获取数据的汇总信息，例如某字段行数、某字段平均值、某字段中最大最小数等

                【标准语法】group by
                    select 字段名1
                    from 表名
                    [where 表达式]
                    [group by 字段名1]
                    [order by 字段名 asc|desc]
                    [limit [位置偏移量,]行数]

                【语法解释】
                    group by 字段名 规定依据哪个字段分组聚合
                    group by核心子句是可选项，使用该子句是为了依据相同字段值分组后进行聚合运算，常和聚合函数联用


            【总结】
                聚合函数

                标准语法
                    select 字段名1,聚合函数(字段名)
                    from 表名
                    [where 表达式]
                    [group by 字段名1]
                    [order by 字段名 asc|desc]
                    [limit [位置偏移量,]行数]



        主知识点六：having&简单运行原理
            【知识点引入】
                【标准语法】
                    select 字段名
                    from 表名
                    [where 表达式]
                    [group by 字段名]
                    [having 表达式]
                    [order by 字段名 asc|desc]
                    [limit [位置偏移量,]行数]

                【语法解释】
                    having 表达式 限定分组聚合后的查询行必须满足的条件
                    having核心子句是可选项，使用该子句是为了对group by分组后的数据进行筛选


            【总结】
                标准语法
                    select 字段名
                    from 表名
                    [where 表达式]
                    [group by 字段名]
                    [having 表达式]
                    [order by 字段名 asc|desc]
                    [limit [位置偏移量,]行数]

                运行原理
                    from--where--group by--having--order by--limit--select



        主知识点七：部分常见函数
            【知识点引入】
                【数学函数】
                    round(x,y)——四舍五入函数
                        round函数对x值进行四舍五入，精确到小数点后y位
                        y为负值时，保留小数点左边相应的位数为0，不进行四舍五入
                        例如：round(3.15,1)返回3.2，round(14.15,-1)返回10


                【字符串函数】
                    concat(s1,s2,...)——连接字符串函数
                        concat函数返回连接参数s1、s2等产生的字符串
                        任一参数为null时，则返回null
                        例如：concat('My',' ','SQL')返回My SQL，concat('My',null,'SQL')返回null

                    replace(s,s1,s2)——替换函数
                        replace函数使用字符串s2代替s中所有的s1
                        例如：replace('MySQLMySQL','SQL','sql')返回MysqlMysql

                    left(s,n)、right(s,n)&substring(s,n,len)——截取字符串一部分的函数
                        left函数返回字符串s最左边n个字符
                        right函数返回字符串s最右边n个字符
                        substring函数返回字符串s从第n个字符起取长度为len的子字符串，n也可以为负值，则从倒数第n个字符起取长度为len的子字符串，没有len值则取从第n个字符起到最后一位
                        例如：left('abcdefg',3)返回abc，right('abcdefg',3)返回efg，substring('abcdefg',2,3)返回bcd，substring('abcdefg',-2,3)返回fg，substring('abcdefg',2)返回bcdefg


                【数据类型转换函数】
                    cast(x as type)——转换数据类型的函数
                        cast函数将一个类型的x值转换为另一个类型的值
                        type参数可以填写char(n)、date、time、datetime、decimal等转换为对应的数据类型


                【日期时间函数】
                    year(date)、month(date)&day(date)——获取年月日的函数
                        date可以是年月日组成的日期，也可以是年月日时分秒组成的日期时间
                        year(date)返回日期格式中的年份
                        month(date)返回日期格式中的月份
                        day(date)返回年日期格式中的日份
                        例如：year('2021-08-03')返回2021，month('2021-08-03')返回8，day('2021-08-03')返回3

                    date_add(date,interval expr type)&date_sub(date,interval expr type)——对指定起始时间进行加减操作
                        date用来指定起始时间
                        date可以是年月日组成的日期，也可以是年月日时分秒组成的日期时间
                        expr用来指定从起始时间添加或减去的时间间隔
                        type指示expr被解释的方式，type可以可以是以下值
                            主要使用红框中的值

                        date_add函数对起始时间进行加操作，date_sub函数对起始时间进行减操作
                        例如：date_add('2021-08-03 23:59:59',interval 1 second)返回2021-08-04 24:00:00，date_sub('2021-08-03 23:59:59',interval 2 month)返回2021-06-03 23:59:59

                    datediff(date1,date2)——计算两个日期之间间隔的天数
                        datediff函数由date1-date2计算出间隔的时间，只有date的日期部分参与计算，时间不参与
                        例如：datediff('2021-06-08','2021-06-01')返回7，datediff('2021-06-08 23:59:59','2021-06-01 21:00:00')返回7，datediff('2021-06-01','2021-06-08')返回-7

                    date_format(date,format)——将日期和时间格式化
                        date_format函数根据format指定的格式显示date值
                        可以换使用的格式有

                        例如：date_format('2018-06-01 16:23:12','%b %d %Y %h:%i %p')返回Jun 01 2018 04:23 PM，date_format('2018-06-01 16:23:12','%Y/%d/%m')返回2018/01/06


                【条件判断函数】——根据满足不同条件，执行相应流程
                    if(expr,v1,v2)
                        如果表达式expr是true返回值v1，否则返回v2
                        例如：if(1<2,'Y','N')返回Y，if(1>2,'Y','N')返回N

                    case when
                        case expr when v1 then r1 [when v2 then r2] ...[else rn] end
                            例如：case 2 when 1 then 'one' when 2 then 'two' else 'more' end 返回two
                            case后面的值为2，与第二条分支语句when后面的值相等相等，因此返回two

                        case when v1 then r1 [when v2 then r2]...[else rn] end
                            例如：case when 1<0 then 'T' else 'F' end返回F
                            1<0的结果为false，因此函数返回值为else后面的F




            【总结】
                【数学函数】
                    round(x,y)——四舍五入函数

                【字符串函数】
                    concat(s1,s2,...)——连接字符串函数
                    replace(s,s1,s2)——替换函数
                    left(s,n)——从左截取字符串一部分的函数
                    right(s,n)——从右截取字符串一部分的函数
                    substring(s,n,len)——从指定位置截取字符串一部分的函数

                【数据类型转换函数】
                    cast(x as type)——转换数据类型的函数

                【日期时间函数】
                    year(date)——获取年的函数
                    month(date)——获取月的函数
                    day(date)——获取日的函数
                    date_add(date,interval expr type)——对指定起始时间进行加操作
                    date_sub(date,interval expr type)——对指定起始时间进行减操作
                    datediff(date1,date2)——计算两个日期之间间隔的天数
                    date_format(date,format)——将日期和时间格式化

                【条件判断函数】——根据满足不同条件，执行相应流程
                    if(expr,v1,v2)
                    case when
                        case expr when v1 then r1 [when v2 then r2] ...[else rn] end
                        case when v1 then r1 [when v2 then r2]...[else rn] end





    【高级语句】
        主知识点八：窗口函数
            【知识点引入】
                【标准语法】
                    窗口函数over([partition by 字段名] [order by 字段名 asc|desc])

                【语法讲解】
                    over()中两个子句为可选项，partition by指定分区依据，order by指定排序依据

                【排序窗口函数】
                    rank()over()
                    dense_rank()over()
                    row_number()over()

                【偏移分析函数】
                    lag(字段名,偏移量[,默认值])over()
                    lead(字段名,偏移量[,默认值])over()


            【总结】
                【排序窗口函数语法】
                    rank()over([partition by 字段名] order by 字段名 asc|desc)
                    dense_rank()over([partition by 字段名] order by 字段名 asc|desc)
                    row_number()over([partition by 字段名] order by 字段名 asc|desc)

                【偏移分析函数语法】
                    lag(字段名,偏移量[,默认值])over([partition by 字段名] order by 字段名 asc|desc)
                    lead(字段名,偏移量[,默认值])over([partition by 字段名] order by 字段名 asc|desc)



        主知识点九：表连接
            【知识点引入】
                【基础语法】
                    内连接
                        select 字段名
                        from 表名1 inner join 表名2 on 表名1.字段名 =  表名2.字段名
                        注意内连接inner可以省略，直接使用join默认为内连接

                    左连接
                        select 字段名
                        from 表名1 left join 表名2 on 表名1.字段名 =  表名2.字段名

                    右连接
                        select 字段名
                        from 表名1 right join 表名2 on 表名1.字段名 =  表名2.字段名



            【总结】
                【内连接inner join语法】
                    select 字段名
                    from 表名1 inner join 表名2 on 表名1.字段名 =  表名2.字段名
                    注意内连接inner可以省略，直接使用join默认为内连接

                【左连接left join语法】
                    select 字段名
                    from 表名1 left join 表名2 on 表名1.字段名 =  表名2.字段名

                【右连接right join语法】
                    select 字段名
                    from 表名1 right join 表名2 on 表名1.字段名 =  表名2.字段名



        主知识点十：子查询
            【知识点引入】
                子查询本身就是一段完整的查询语句，然后用括号英文括号()包裹嵌套在主查询语句中，子查询可以多层嵌套
                最常用的子查询运用在from和where子句中

            【总结】
                子查询本身是一个完整的查询，由括号包裹嵌套在主查询中
                子查询最后返回查询出的结果给主查询
                子查询可以在select，from，where，having子句（同where）中使用，但要注意不同子句能接受的子查询种类有差别
                子查询可以多重嵌套（子查询可以作为主查询再嵌套子查询）




