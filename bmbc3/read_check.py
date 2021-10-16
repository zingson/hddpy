import sys,gmssl
from gmssl import sm2
from gmssl.sm3 import sm3_hash
from base64 import b64encode, b64decode
from gmssl.func import bytes_to_list,list_to_bytes
import os, sys
import rsa


    
sm3_f_name = input("your file name: ")
#sm3_f_name='to_unipay_权益白名单0903.txt'
#重新解密

data_file = open(sm3_f_name,"r",encoding="UTF-8")
content = data_file.read()
content=content.strip()

varstr = content.split('=====')

f_content = varstr[0].strip()
zy_contenet = varstr[1].strip()

#print("【文件内容】\n"+f_content)
print("【签名】\n"+zy_contenet)



with open('cmbc_public.pem','r') as f:
  pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

is_ver=rsa.verify(f_content.encode(encoding="utf-8"), bytes.fromhex(zy_contenet), pubkey)

if is_ver :
    print("文件正确\n")
    ck_file_name = "checked_"+sm3_f_name
    ck_file = open(ck_file_name,"w",encoding="UTF-8")
    ck_file.write(f_content)
    ck_file.close()
    
else:
    print("文件错误正确\n")





