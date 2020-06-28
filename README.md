# olm-analysis

Parse dumped Mac OLM file and analysis it and use pyecharts to to data display.

本来想用 echarts 实现的，但是中间出了很多波折，最后还是决定把这个项目当作 python 数据分析的实践项目，顺便学一下 numpy, panda 等库好了。

## OLM 文件解析

在 Mac 的文件系统中，outlook 的导出文件是 `.olm` 文件。这种 type 是 Mac 独有的，解析起来并不难。你可以用解压缩(unzip)的方式打开它。解压之后你会看到一组文件夹。概览它你会发现邮件被存放在 Accounts 下的 com.microsoft.__Messages 下的 xml 文件中。解压文件夹结构如下：

```txt
Outlook\ for\ Mac\ Archive
├── Accounts
│   └── Jack
│       ├── Contacts
│       │   └── Skype\ for\ Business\ Contacts
│       ├── Suggested\ Contacts
│       └── com.microsoft.__Messages
│           ├── Folder01
│           │   └── com.microsoft.__Attachments
│           ├── Folder02
│           │   └── com.microsoft.__Attachments
│           ├── Folder03
│           │   ├── Folder04
│           │   │   └── com.microsoft.__Attachments
│           │   ├── Folder05
│           │   └── com.microsoft.__Attachments
│           ├── Junk\ E-Mail
│           ├── RSS\ Feeds
│           ├── Sent\ Items
│           │   └── com.microsoft.__Attachments
│           └── Sync\ Issues
│               ├── Conflicts
│               ├── Local\ Failures
│               └── Server\ Failures
└── Local
    ├── Address\ Book
    └── com.microsoft.__Messages
        ├── Deleted\ Items
        ├── Drafts
        ├── Inbox
        ├── Outbox
        ├── Sent\ Items
        └── Spam\ Email
```

xml 文件的定义可以参考 git repo OLMReader 中 [email.xsd](https://github.com/teverett/OLMReader/blob/master/src/main/resources/schema/emails.xsd) 的定义。

## 常用包

* matplotlib 可视化 - 画图
* numpy 处理数据
* pandas 处理非值形数据

pandas 在功能上要比 numpy 强很多，整合了很多数据库类似的操作，比如 merge, join, group 等 还有一些 index 之类的东西

## 方法

df.desciber() 很方便，显示大体信息
df.head()
df.info()
df.sort_values() 排序

## 表示连续数据: 直方图，箱型图

区别：直方图可以表现出趋势，比如双峰形，箱型图不能

统计邮件大小的时候，用箱型图其实不怎么好，应为收集到的数据都是合法的，而且有个别值差异特别大，展现出来的箱子就很难看，而且展示异常值的功能也废了

## Issues

Windows 平台 IPython 终端自动补全会输出很多 warning, workaround as

```python
import warnings
warnings.filterwarnings('ignore')
# warnings.filterwarnings('once')
```