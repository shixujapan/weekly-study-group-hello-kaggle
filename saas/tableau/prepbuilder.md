流程如下
   
   
   1.1 制作路径文件
        复制粘贴课程淘pv数据文件夹下0504的任意表格，修改A1单元格，删除数据填0命名为0000路径文件.csv，另存为csv-utf-8格式

    1.2 prep builder连接并输入多个文件
        打开TPB软件，连接到文本文件(csv)，选择文件夹淘宝pv数据中的0000路径文件.csv
            选择多个文件，通配符并集，文件选择排除，匹配模式填写0000路径文件*
            如果要指定导入哪个品牌的表格，文件选择包括，匹配模式填写类似*byhe*


    2.数据清理
        在起始点后点击加号，添加清理步骤为淘宝pv数据，对数据进行处理
        2.1 创建计算字段
            流量日期
                DATE(DATEADD('day',-1,NOW()))
                由于导入的是0504的数据，所以需要将流量日期这里暂时修改为'2021-05-04'

            ClientName
                IF CONTAINS([File Paths],'byhe') THEN 'byhe'
                ELSEIF (CONTAINS([File Paths],'pcbd') OR CONTAINS([File Paths],'mh') OR CONTAINS([File Paths],'qzx')OR CONTAINS([File Paths],'sfks')) THEN 'pcbd'
                ELSEIF CONTAINS([File Paths],'mx') THEN 'mxwl'
                END


        2.2 删除字段
            File Paths

        2.3 更改字段类型
            更改 商品ID 的数据格式 → 字符串
            更改 流量日期 的数据格式 → 字符串


    3.输出和创建表
        3.1 输出到表
            在淘宝pv数据后点击加号，添加输出步骤为输出到表
                同样输出为文件，类型为csv，保存到文件夹淘宝pv数据，20210504taopv.csv
                    点击运行流程



        3.2 构架数据库表
            打开datagrip，通过处理好的表格构架数据库表
                右键doutaodata，从文件导入数据
                    命名表格为taobaopv
                    确认字段类型

                点击ddl预览，添加自增主键
                    自增主键代码
                        自增主键 int unsigned not null auto_increment primary key,


                点击导入，并确认数据成功导入
                    确认流量日期含有完整的2021



        3.3 输出到库
            在淘宝pv数据后点击加号，添加输出步骤为输出到库
                连接自己的个人数据库，选择数据库doutaodata，表taobaopv
                    确保除了自增主键外其他字段和类型都可以对上




    4.数据验证
        添加聚合步骤，查看对应金额总和
            流量日期到分组
            综合成交金额到总和


    5.验证流程
        5.1 保存工程文件及备份
            保存TPB流程为taobaopv数据流程.tfl，关闭流程

            将文件夹分时数据中的文件除0000路径文件进行备份，除0000路径文件外清空文件夹

        5.2 导入新的原始数据
            将日期为0505的淘宝pv表复制到文件夹淘宝pv数据
            点开每个工作簿，重命名每个工作簿表格中的A1单元格为推广单元名称，并另存为csv utf-8格式

        5.3 验证TPB流程
            再次打开TPB流程，能正确打开进入流程界面表示文件读取正常
            点击淘宝pv数据，修改字段流量日期
                流量日期
                    由于导入的是0505的数据，所以需要将流量日期这里暂时修改为date('2021-05-05')


            输出到库前查看流量日期是否为对应的日期，字段是否都一一对应

        5.4 输出到库/表
            确认后，运行流程

            到datagrip中输入sql代码验证数据入库成功，备份数据
                数据正常入库
                    select
                    ClientName
                    ,流量日期
                    ,sum(综合成交金额)
                    from doutaodata.taobaopv
                    group by 1,2
                    order by 1,2
