import os
import xml.etree.ElementTree as ET 


class Email:
    def __init__(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
        subjectnode = [node for node in root.iter('OPFMessageCopySubject')][0]
        self.subject = subjectnode.text
        
        fromnode = [node for node in root.iter('OPFMessageCopyFromAddresses')][0]
        self.fromnode.find('emailAddress').attrib['OPFContactEmailAddressAddress']
        
        ccnodes = [node for node in root.iter('OPFMessageCopyCCAddresses')]
        if ccnodes:
            self.cc = [sub.attrib['OPFContactEmailAddressAddress'].lower() for sub in ccnodes[0]]

        tonodes = [node for node in root.iter('OPFMessageCopyToAddresses')]
        self.to = [sub.attrib['OPFContactEmailAddressAddress'].lower() for sub in tonodes[0]]
        self.size = os.path.getsize(path)
        receivedtimenode = [node for node in root.iter('OPFMessageCopyReceivedTime')][0]
        # time sample: 2018-11-15T03:21:13
        self.receive_date = receivedtimenode.text

    def __repr__(self):
        return 'Sub: %s, Sender: %s' % (self.subject, self.receive_from)


def serialize_email(obj):
    if isinstance(dict, Email):
        return obj.__dict__
    else:
        raise TypeError

'''
统计所有的邮件大小画出 箱形图
'''