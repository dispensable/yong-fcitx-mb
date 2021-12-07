with open("./yong-mb-py.txt") as f:
    with open("./result.txt", "w") as f1:
        start_data = False
        for i in f:
            if i == '[Data]\n':
                start_data = True
                f1.write(i)
                continue
            if start_data:
                j, r = i.split(" ", 1)
                print(f"r: {r}")
                words = r.strip("\n").split(" ")
                for w in words:
                    f1.write(f"{j}\t{w}\n")
            else:
                f1.write(i)
