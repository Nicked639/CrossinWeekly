# python3
# encoding: utf-8
s1 = "我们在一起吧"
s2 = "我选择原谅你"
s3 = "别说话，吻我"
s4 = "多喝热水"
import hashlib
import base64
l = [s1, s2, s3, s4]
def main():
    for i in l:
        i_utf8 = i.encode('utf-8')
        i_md5 = hashlib.md5(i_utf8)
        i_md5_byte = bytes(i_md5.hexdigest(), 'utf-8')
        i_bs64 = base64.b64encode(i_md5_byte)
        print(i, i_bs64.decode())

if __name__ == '__main__':
    main()
