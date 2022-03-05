class schedule():
    def __init__(self):
        f = open("datafile","r")
        self.day = int(f.read())
        f.close()
    def clear(self):
        with open("datafile","r+") as f:
            f.truncate()
            f.write("0")
        self.ok = "已清除"
    def add(self):
        with open("datafile","r+") as f:
            num = self.day + 1
            f.truncate()
            f.write(str(num))
    def done(self):
        self.add()
        self.kp = f"已坚持{self.day+1}天"
