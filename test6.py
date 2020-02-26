

def getInfo():
    var1 = input("\nPlease provide first numeric value: ")
    var2 = input("\nPlease provide second numeric value: ")
    return var1, var2


def compute():
    go = True
    while go:
        var1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            print("{} + {} = {}".format(var1, var2, var3))
            go = False
        except ValueError as e:
            print("{}: You did not provide a numeric value".format(e))
        except:
            print("Oppps, something went horribly wrong and it is most likely your fault. Good Job!")



if __name__ == "__main__":
    compute()