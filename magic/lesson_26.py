class Test:
    def test1(self):
        print("123")

class Test2(Test):
    def test1(self):
        super().test1()
        print("999")

    def aaa(self):
            super().test1()


i