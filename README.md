# olm-analysis

Parse dumped Mac OLM file and analysis it and use pyecharts to to data display.

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

xml 为难的定义可以参考 git repo OLMReader 中 [email.xsd](https://github.com/teverett/OLMReader/blob/master/src/main/resources/schema/emails.xsd) 的定义。
