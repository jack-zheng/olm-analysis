import os
import glob
import json
import xml.etree.ElementTree as ET

from dotenv import load_dotenv


load_dotenv()


def extract_email_address(root, file_key):
    nodes = [node for node in root.iter(file_key)]
    addresses = []
    for sub in nodes:
        for addr_element in sub.iter('emailAddress'):
            if 'OPFContactEmailAddressAddress' in addr_element.attrib:
                addresses.append(addr_element.attrib['OPFContactEmailAddressAddress'])
    
    return addresses


class Email:
    def __init__(self, path):
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            subjectnode = [node for node in root.iter('OPFMessageCopySubject')]
            self.subject = subjectnode[0].text if subjectnode else ''
            self.receive_from = extract_email_address(root, 'OPFMessageCopyFromAddresses')
            self.cc = extract_email_address(root, 'OPFMessageCopyCCAddresses')
            self.to = extract_email_address(root, 'OPFMessageCopyToAddresses')
            self.size = os.path.getsize(path)
            receivedtimenode = [node for node in root.iter('OPFMessageCopyReceivedTime')][0]
            # time sample: 2018-11-15T03:21:13
            self.receive_date = receivedtimenode.text
        except Exception:
            print("Exception throw when process file: %s" % path)
            raise Exception

    def __repr__(self):
        return 'Sub: %s, Sender: %s' % (self.subject, self.receive_from)


def serialize_email(obj):
    if isinstance(obj, Email): 
        return obj.__dict__ 
    else: 
        raise TypeError    


def unser_email(dict): 
    tmp = Email.__new__(Email) 
    tmp.__dict__ = dict
    return tmp


def fetch_emails():
    for filename in os.listdir(current_folder):
        if not filename.endswith(".xml"):
            print(current_folder+"/"+filename+" is not xml")
            continue


def in_exclude_folder(path): 
    for sub in ['Sent Items', 'Sync Issues']: 
        if sub in path: 
            return True 
    return False


msg_folder = os.getenv('msg_folder')


def cache_email():
    files = [f for f in glob.glob(msg_folder + "**/*.xml", recursive=True) if not in_exclude_folder(f)]
    emails = [Email(fp) for fp in files]
    with open('dump.json', 'w') as file:
        json.dump(emails, file, default=serialize_email, indent=2)


if __name__ == '__main__':
    cache_email()


'''
统计所有的邮件大小画出 箱形图
'''