from simplecrypt import decrypt, DecryptionException

with open('/home/e-golov/Downloads/encrypted.bin', 'rb') as data, open('/home/e-golov/Downloads/passwords.txt', 'r') as pwds:
    encData = data.read()
    # print(encData)

    for i, pwd in enumerate(pwds):
        pwd = pwd.rstrip()
        with open('/home/e-golov/tmp/res_{}.txt'.format(i), 'w') as out:
            try:
                out.write(decrypt(pwd, encData).decode("utf-8"))
            except DecryptionException as e:
                print('Error for {} password'.format(i))


