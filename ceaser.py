

class ceaser:
    def __init__(self):
        self.letters = "abcdefgğhıjklmnoprsştuvyz"


        def encode ( self ,text , chipcher ):
            rText = ""
            for i in text:
                counter = 0
                for j in self.letters:
                    if i == j:
                        if (counter + chipcher) > len(self.letters):
                            rText += self.letters[(counter + chipcher)] - len(self.letters) ]
                        else:
                            rText += self.letters[(counter + chipcher)]
                        break
                    counter +=1
            return rText


if name == " main ":
    cs = ceaser()
    ans = cs.encode (" bu gece 2 de aynı yerde " , 5)
    print("şifrelenmiş hali: ", ans  )
