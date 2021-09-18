import sys,gmssl
from gmssl import sm2
from gmssl.sm3 import sm3_hash
from base64_test import b64encode, b64decode
from gmssl.func import bytes_to_list,list_to_bytes
import os, sys


# sm2的公私钥(16进制)
SM2_PRIVATE_KEY = '6178d0e3f26010ca1297d32fde9d1ef152c7e04509d0d6e96ca69d39a3714223'
SM2_PUBLIC_KEY = '8f5ba7cf46a602e73422c016fad50fba88febf5dae4813bd45752a3ffc7eb3cf0accc91fee7004b0643c783b32e8a4222979be6e0322e27c27e57439dda7d493'

sm2_crypt = sm2.CryptSM2(public_key=SM2_PUBLIC_KEY, private_key=SM2_PRIVATE_KEY)

# 加密
def encrypt(info):
    encode_info = sm2_crypt.encrypt(info.encode(encoding="utf-8"))
    encode_info = b64encode(encode_info).decode()  # 将二进制bytes通过base64编码
    return encode_info


# 解密
def decrypt(info):
    decode_info = b64decode(info.encode())  # 通过base64解码成二进制bytes
    decode_info = sm2_crypt.decrypt(decode_info).decode(encoding="utf-8")
    return decode_info


def str2byte(msg):  # 字符串转换成byte数组
    ml = len(msg)
    msg_byte = []
    msg_bytearray = msg  # 如果加密对象是字符串，则在此对msg做encode()编码即可，否则不编码
    for i in range(ml):
        msg_byte.append(msg_bytearray[i])
    return msg_byte


def byte2str(msg):  # byte数组转字符串
    ml = len(msg)
    str1 = b""
    for i in range(ml):
        str1 += b'%c' % msg[i]
    return str1.decode('utf-8')
   
#文件要求，UTF-8编码，第一行是标题，每行一条记录
#每行记录中，第一列是手机号，需要sm3加密。
#对文件先base64编码，然后使用sm3生成摘要，然后对摘要进行sm2加密。接收方需要对文件与摘要的正确性进行校验。


#对原文件手机号进行sm3加密
f_name = '权益使用情况.txt'
data_file = open(f_name,'r',encoding="UTF-8")

out_f_name = 'to_cmbc_'+f_name
outf = open(out_f_name,"w",encoding="UTF-8")

content = data_file.read()
content=content.strip()

#首先base64编码
str_b64=b64encode(content.encode(encoding="utf-8"))    

#生成sm3摘要
str_sm3 = sm3_hash(bytes_to_list(str_b64))

#对摘要进行sm2加密
str_enc = encrypt(str_sm3)


outf.write(content)
outf.write("\n=====\n")

outf.write(str_sm3+"\n")
outf.write(str_enc+"\n")

data_file.close()
outf.close()














