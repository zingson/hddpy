import base64
import binascii
from gmssl import sm2, func
#16进制的公钥和私钥
private_key = '6178d0e3f26010ca1297d32fde9d1ef152c7e04509d0d6e96ca69d39a3714223'
public_key = '8f5ba7cf46a602e73422c016fad50fba88febf5dae4813bd45752a3ffc7eb3cf0accc91fee7004b0643c783b32e8a4222979be6e0322e27c27e57439dda7d493'
sm2_crypt = sm2.CryptSM2(public_key=public_key, private_key=private_key)


data = "123" # bytes类型
random_hex_str = func.random_hex(sm2_crypt.para_len)
sign = sm2_crypt.sign(data.encode(encoding="utf-8"), random_hex_str) #  16进制
print(" 签名结果")
print(sign)

#sign = "3045022100b882ca9dab9d7d3f968f690a25248a433e8f083bfdea601201b4760d1214a4ce0220344d84269ecc40737082c2b4f27d8f6862fef50e68155036cbd2dfbf94b6ec2c"
signRs = sm2_crypt.verify(sign, data.encode(encoding="utf-8")) #  16进制
print(" 验签结果")
print(signRs)
print(" 原始数据")
print(data)
