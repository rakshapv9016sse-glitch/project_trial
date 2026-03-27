class device:
    def methodpower_on(self):
        print("device:power ON")
class laptop(device):
    def method_coding(self):
        print("laptop is used for coding")
class mobile(device):
    def methodcall(self):
        print("mobile is used for calling")

a=laptop()
b=mobile()
a.methodpower_on()
a.method_coding()
b.methodpower_on()
b.methodcall()
