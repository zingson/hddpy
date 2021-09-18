from base64 import b64encode, b64decode

s = """
客户唯一ID,客户手机,批次,券类型,券数量
待定,dfb9696c3cdeb8a068fadf4ad6d7a14fba30658cbb2219f1c1f0f4018a769199,2021-09-14,券类型,1
待定,d5a25ed65ccf263de69be6f1a21e357ce71c7a56c5c29c58606195630d0a4721,2021-09-14,券类型,1
"""
s = s.strip()
print(b64encode(s.encode(encoding='utf-8')))
