class personel:
    adi="ilkad"
    def __init__(self):
        pass
    #def __init__(self,ad):
     #   self.adi=ad
      #  print(self.adi)

    def get_adi(self):
        return self.adi

    def set_adi(self,ad):
        self.adi=ad

    def print_adi(self):
        print(self.adi)
class mudur:
    def __init__(self):
        print("Müdür")


def printme():
    print("Yazdı")