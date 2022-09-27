
           
import random

def main():
    """Start a elements guessing game."""
    print("Guess the elements!")

    periodic = [
        "zinc",
        "integer",
        "gallium",
        "bromine",
        "livermorium",
        "thulium",
        "curium"
        "plutonium"
        "hassium"
        ]

    x = random.choice(periodic)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What elements am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        elif x=="zinc":
            print("Muncul gejala mirip {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
        elif x=="gallium":
            print("Pemukaan yang retak melengkung seperti cangkang laut {}. Unfortunalety you got the wrong answer. Please Try again!".format (guess))
        elif x=="bromine":
            print("berat atom:79.90) {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
        elif x=="livermorium":
            print("berat aton 293)  {}. Unfortunalety you got the wrong answer.Please try again!".format(guess))
        elif x=="integer":
            print("salah satu jenis tipe data primitif yang secara standar sudah terdenfensi pada satu bahasa peprograman  {}. Unfortunalety  you got the wrong answer. Please Try again!".format (guess))
        elif x=="thulium":
            print("thulium ialah bukan toksik) {}. Unfortunalety you got the wrong answer.Please try again!".format(guess))
        elif x=="curium":
            print("berwarna putih keperakkan) {}. Unfortunalemy you got the wrong answer. Please Try again!".format(guess))
        elif x=="plutonium":
            print("satu unsur kimia dalam table periodic yang memiliki lambang Pu) {}. Unfortunalemy you got the wrong answer. please try again!".format(guess))
        elif x=="hassium":
            print("ditemukan oleh Peter Ambruseter. Gottiried Muzenber dan kawan kawan di GSI darmstadt Jerman pada tahun 1984 {}. Unfortunalety you got the wrong answer. Please try again!".format(guess))
            
                  
                  
        
main()
