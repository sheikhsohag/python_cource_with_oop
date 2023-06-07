class phone:
    price = 12000
    color = 'blue'
    btand = 'samsung'
    features = ['cemera', 'speaker']
    def call(self):                       #it is nessecery to give self to to the function.  it is always exist
        print('calling one person')

    def send_sms(self,phone,sms):
        text = f'sending sms to: {phone} and message: {sms}'
        return text   

my_phone = phone()
print(my_phone.features)
my_phone.call()

result = my_phone.send_sms(12345,'i forgot to miss u')
print(result)
