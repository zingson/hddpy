import sys, gmssl
from gmssl import sm2
from gmssl.sm3 import sm3_hash
from base64 import b64encode, b64decode
from gmssl.func import bytes_to_list, list_to_bytes
import os, sys

# sm2的公私钥(16进制)
SM2_PRIVATE_KEY = ''
SM2_PUBLIC_KEY = 'fea65b9fd9d416d471273180462f529c1f46cd68038b14795f3cd5c9b7ed014ae461ef51a2db77dcf62337cfe01172790645997e0d6c0d1741e84b2c34fff595'

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


sm3_f_name = input("your file name: ")
# sm3_f_name='to_unipay_权益白名单0903.txt'
# 重新解密

data_file = open(sm3_f_name, "r", encoding="UTF-8")
content = data_file.read()
content = content.strip()

varstr = content.split('=====')

f_content = varstr[0].strip()
zy_contenet = varstr[1].strip()

# print("【文件内容】\n"+f_content)
print("【签名】\n" + zy_contenet)

# des_sm3=decrypt(en_str[1])
is_ver = sm2_crypt.verify(zy_contenet, f_content.encode(encoding="utf-8"))  # 摘要与签名验证

# print("【签名解密】\n"+ des_sm3)

if is_ver:
    print("文件正确\n")
    ck_file_name = "checked_" + sm3_f_name
    ck_file = open(ck_file_name, "w", encoding="UTF-8")
    ck_file.write(f_content)
    ck_file.close()

else:
    print("文件错误正确\n")





