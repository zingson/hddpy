import sys, gmssl
from gmssl import sm2
from gmssl.sm3 import sm3_hash
from base64 import b64encode, b64decode
from gmssl.func import bytes_to_list, list_to_bytes
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
    e = info.encode()
    decode_info = b64decode(e)  # 通过base64解码成二进制bytes
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


# sm3_f_name = input("your file name: ")
# sm3_f_name='to_unipay_权益白名单0903.txt'
sm3_f_name = 'YHK_MS_20210922.txt'
# 重新解密

data_file = open(sm3_f_name, "r", encoding="UTF-8")
content = data_file.read()
content = content.strip()

varstr = content.split('=====')

f_content = varstr[0].strip()
zy_contenet = varstr[1].strip()

print("【文件内容】\n" + f_content)
print("【摘要及签名】\n" + zy_contenet)

en_str = zy_contenet.split('\n')
# print(en_str)
# print(en_str[1])
# print(en_str[2])

str_b64 = b64encode(f_content.encode(encoding="utf-8"))
print("【Base64】")
print(str_b64)
# print("【Base64】\n"+bytes_to_list(str_b64))
str_sm3 = sm3_hash(bytes_to_list(str_b64))
str_enc = encrypt(str_sm3)

print("【重新计算摘要】\n" + str_sm3)
# print("【重新计算签名】\n"+str_enc)

des_sm3 = decrypt(en_str[1])
print("【签名解密】\n" + des_sm3)

if str_sm3 == des_sm3:
    print("文件正确\n")
else:
    print("文件错误正确\n")

print("\n摘要test：" + sm3_hash(bytes_to_list(b64encode("test".encode(encoding="utf-8")))))
