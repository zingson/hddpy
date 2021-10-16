import sys,gmssl
from gmssl import sm2
from gmssl.sm3 import sm3_hash
from base64 import b64encode, b64decode
from gmssl.func import bytes_to_list,list_to_bytes,random_hex
import os, sys
import rsa


   
#文件要求，UTF-8编码，第一行是标题，每行一条记录
#每行记录中，第一列是手机号，需要sm3加密。
#对文件先base64编码，然后使用sm3生成摘要，然后对摘要进行sm2加密。接收方需要对文件与摘要的正确性进行校验。


#原文件：
#客户号,手机号,变形客户号,加密后手机号,批次号,券类型编号,客户标识,券数量,有效期,券产品编号,
#输出文件：
#变形客户号,加密后手机号,批次号,券类型编号,券数量,有效期,券产品编号
#对原文件手机号进行sm3加密
f_name = input("your file name: ")
data_file = open(f_name,'r',encoding="UTF-8")

out_f_name = 'tmp_'+f_name
outf = open(out_f_name,"w",encoding="UTF-8")

sm3_f_name = 'YHK_MS_'+f_name
sm3f = open(sm3_f_name,"w",encoding="UTF-8")

cmbc_name = 'to_cmbc_'+f_name
cmbcf = open(cmbc_name,"w",encoding="UTF-8")

line = data_file.readline().replace('\n','')
varstr = line.split(',')
tmp_line = ','.join([varstr[2],varstr[3],varstr[4],varstr[5],varstr[7],varstr[8],varstr[9]])
outf.write(tmp_line+"\n")
cmbc_line = line
cmbcf.write(cmbc_line+"\n")

line = data_file.readline().replace('\n', '')
while line:
    varstr = line.split(',')
    phone=varstr[1]
    sm3_phone = sm3_hash(bytes_to_list(phone.encode(encoding="utf-8")))
    #print(sm3_phone)
    varstr[3]=sm3_phone
    tmp_line = ','.join([varstr[2],varstr[3],varstr[4],varstr[5],varstr[7],varstr[8],varstr[9]])
    outf.writelines(tmp_line+"\n")
    
    cmbc_line=','.join(varstr)
    cmbcf.write(cmbc_line+"\n")
    
    line = data_file.readline().replace('\n', '')
    
data_file.close()
outf.close()
cmbcf.close()

#读入对手机号加密后的中间文件
data_file=open(out_f_name,'r',encoding="UTF-8")
content = data_file.read()
content = content.strip()  #去除头尾空行


sm3f.write(content)
sm3f.write("\n=====\n")

#print("【文件内容】\n"+content)

#对文件内容进行签名
#str_enc = encrypt(str_sm3)
#random_hex_str = random_hex(sm2_crypt.para_len)
#str_enc = sm2_crypt.sign(content.encode(encoding="utf-8"), random_hex_str) #  16进制
with open('cmbc_private.pem','r') as f:
  privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
str_enc = rsa.sign(content.encode(encoding="utf-8"), privkey, 'SHA-1').hex()

print("【对内容签名】\n"+str_enc)

sm3f.write(str_enc+"\n")
sm3f.close()
data_file.close()













