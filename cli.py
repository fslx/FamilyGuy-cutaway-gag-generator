print(r"Welcome to the Family Guy joke creator, create any Family Guy cutaway-gag you'd like, simply input the charachter you'd like in your joke, and the program with create it")
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
choice = float(input())
if choice == 1:
    import Familyguy
    Familyguy.main()
elif choice != 1:
    import Simpleguy
    Simpleguy.main()
elif choice != 1 or 2:
    pass
    exit()
# ^Less lines of code doing the same job as previous version.
