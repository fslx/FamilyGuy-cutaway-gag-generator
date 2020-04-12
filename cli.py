print(r"Welcome to the Family Guy joke creator, create any Family Guy cutaway-gag you'd like, simply input the charachter you'd like in your joke, and the program will create it")
print(r"""

          ⠀⠀⠀⠀⡠⠔⠒⠉⢉⣉⣙⣒⣠⣀
        ⠀⠀⠀⢠⠊⠐⡞⢩⣭⣭⣭⣀⡔⣒⡚⠇
        ⠀⠀⠠⠁⠀⠀⠉⢿⡘⠃⣸⠃⠓⠒⢦⠌⢦⡀
        ⠀⢀⠇⠀⠀⠀⠀⠠⢍⡉⠁⠐⠦⠤⠞⡀⠀⠀⢣
        ⠀⠘⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠉⠉⢳⠄⠀⠸⡆
        ⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⠁⠀⠀⠀⠀⡇
        ⠀⡇⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⡇
        ⡠⡇⠀⠀⠀⠀⠀⠀⠀⢷⣄⣀⡴⣤⣀⠴⠁⠀⠀⡇
        ⢣⠘⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏
        ⠀⠑⣄⠈⠢⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⡰
        ⠀⠀⠈⠑⢄⡀⠁⠢⢄⡀⠀⠀⠀⠀⠀⢀⡠⠒⢁⠔
        ⠀⠀⠀⠀⠀⠈⠒⠤⣀⠀⠉⠒⡂⢤⡰⠫⣄⡰⠃
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠼⠀⠠⡷⡀⠈
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱""")
print(r"If you would like a joke scenario with celebrities, press 1) ")
print(r"Otherwise, choose option 2) ")

choice = int(input())

if choice == 1:
    import Familyguy
    Familyguy.main()
if choice == 2:
    import Simpleguy
    Simpleguy.main()
else:
    print("Thanks for using the Family Guy joke creator, hope to see you again!")
    exit()
