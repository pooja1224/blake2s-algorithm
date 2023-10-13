# # password = "abcd@1234"
# # value = hashlib.sha256(password.encode())
# # hexadecimal_value = value.hexdigest()
# # print(hexadecimal_value)
# #
# # # def weather(request):
# # #     url = 'https://api.apis.guru/v2/list.json'
# # #     response = requests.get(url)
# # #     data = response.json()
# # #     return JsonResponse(data)
# #
# # import bcrypt,os
# # s = time.time()
# #
# # password = b"pooja@2002"
# # digest = bcrypt.hashpw(password,bcrypt.gensalt())
# # # if bcrypt.checkpw(password,digest):
# # #     print("matched")
# # # print(digest)
# # e = time.time()
# # r = e-s
# # print(r)
# # #b'$2b$12$ZknnCf7RO00BP5xzyAdcgOKwY5uvN.GiQAv.ZBeVx0bV4eRBjqvM2'
# # # print(hashlib.algorithms_available)
# # # print(hashlib.algorithms_guaranteed)
# # # s = time.time()

# # # password = b"pooja"
# # digest = hashlib.blake2s(a).hexdigest()
# # # digest1 = hashlib.blake2s(a).hexdigest()
# # #
# # # if digest == digest1:
# # #     print('matched')
# # # #559232e91cc0c59b42de96f11dbce6458f09993de25599945d08d7dfc27b3042
# # #
# # #
# # #
# # # print(digest)
# #
# #
# #
# # # h = bcrypt.hashpw(b"pooja",bcrypt.gensalt(rounds=9))
# # # e =time.time()
# # # r = e-s
# # # print(r)
# #
#

# salt = os.urandom(16)
# password = "pooja".encode("utf-8")
# a = salt+password
# digest = hashlib.blake2s(a).hexdigest()
# print(digest)

byte_data = b'\x48\x65\x6c\x6c\x6f'

# Convert to a UTF-8 encoded string
utf8_string = byte_data.decode('utf-8')

# Check the UTF-8 string
print(utf8_string)

reverted_byte_data = utf8_string.encode('utf-8')

# Check the reverted bytes
print(reverted_byte_data)


#views.py

#usersignup -                     # salt = ''.join(random.choices(string.ascii_letters, k=5))+''.join(random.choices(string.punctuation, k=5))
