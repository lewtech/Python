def read_csv(filename):
    text=open(filename,"r").read()
    rows=text.split("\n")
    print(rows[:10])
