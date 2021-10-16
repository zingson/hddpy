from gmssl import sm2
from gmssl.sm3 import sm3_hash
from gmssl.func import bytes_to_list, list_to_bytes, random_hex


# sm2的公私钥(16进制)
SM2_PRIVATE_KEY = '6178d0e3f26010ca1297d32fde9d1ef152c7e04509d0d6e96ca69d39a3714223'
SM2_PUBLIC_KEY = '8f5ba7cf46a602e73422c016fad50fba88febf5dae4813bd45752a3ffc7eb3cf0accc91fee7004b0643c783b32e8a4222979be6e0322e27c27e57439dda7d493'


sm2_crypt = sm2.CryptSM2(public_key=SM2_PUBLIC_KEY, private_key=SM2_PRIVATE_KEY)

content = "123"

#content = sm3_hash(bytes_to_list(content.encode(encoding="utf-8")))
random_hex_str = random_hex(sm2_crypt.para_len)
str_enc = sm2_crypt.sign(content.encode(encoding="utf-8"), random_hex_str)  # 16进制
print("【对内容签名】\n" + str_enc)
