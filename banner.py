from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

def show_banner(banner_choice):
    if banner_choice == 1:
        print(Fore.RED + ''' 
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣧⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣛⡛⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣹⣽⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣷⣦⣌⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣯⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣴⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣾⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⡬⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⣿⣉⣭⣭⣭⡿⣿⣻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡃
⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣤⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⣷⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠻⠿⠿⢿⣿⣿⣟⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣾⡇
⢸⣿⣿⣿⣿⣿⣿⣿⠏⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⡏⢹⣿⣿⣿⡿⠟⠛⠛⠿⣿⣿⣿⣿⣿⠀⠐⠛⠛⠃⠀⢢⠀⢹⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⣾⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⡏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢸⡟⣿⠀⣿⡿⠋⠀⠂⠀⠀⠀⠹⣿⡖⣿⣿⠀⠀⠀⠀⠀⠀⢸⠿⠀⣿⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⡏⢠⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢳⣻⣶⡟⠀⠀⠀⠀⠀⢸⠃⠀⣿⠧⠛⢿⣄⡀⠀⠀⣀⢀⠾⠀⢸⣿⣶⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⠇
⢸⣿⣿⣿⣿⣿⠁⠋⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠹⣻⡇⠀⠀⠀⠀⠀⠘⠀⣰⡏⠀⠀⠀⠻⣿⣶⣤⣉⣉⣠⣴⣿⣿⣿⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⡿⠋⠀⠀
⢸⣿⣿⣿⣿⣿⡇⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠱⢾⡄⠀⠀⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡍⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡼⡄⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⠀⢰⠋⠉⠀⠀⠀⠀⠈⣿⣿⣿⡿⠿⢿⣿⣿⣿⡿⣡⣿⡟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢾⣿⣶⣀⣀⣶⣿⣿⣿⣦⣀⣤⢦⣤⣿⣿⣿⣿⣿⠟⢋⡿⢇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠙⣄⠀⠀⠀
⢸⣿⣿⣿⣿⡿⠃⡄⠀⠀⠀⠰⠀⠀⣠⡯⣽⡛⠀⠀⡀⠈⠻⣿⡧⣾⠏⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⠃⢸⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼⣟⡶⡆
⢸⣿⣿⣿⣿⡇⠸⣿⣦⡀⠀⣀⣠⣾⠟⠃⢿⣧⠀⠀⠁⠘⠀⠘⣇⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠘⢿⡿⣿⣿⣿⣿⣿⣿⠻⣿⣿⣿⡟⢃⣡⡧⠀⣾⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣙⠳⡇
⢸⣿⣿⣿⣿⣿⡶⢈⢛⣿⣿⣿⡿⠋⢀⡆⢸⣿⡀⠀⠦⠄⠀⣸⡇⣴⣿⣿⣿⣿⣿⣿⣿⣿⣛⣿⣷⣶⣷⣶⣾⣍⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠈⠓⠿⡿⣿⡟⣻⢩⣯⣽⣷⠙⠃⠈⠁⢠⠴⡞⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄
⢀⠸⣿⣿⣿⣿⠃⡼⢻⣿⣿⣟⣣⣀⡈⠁⢸⣿⣿⣿⣶⣾⢯⣿⢻⣿⣿⣿⣿⣿⣿⣿⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠁⠑⡓⠛⠃⠉⣈⠉⠀⠀⠀⠀⠀⣀⣾⣾⡐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠸⠆⢻⣿⣿⡟⢰⣷⠀⠪⢝⡻⢿⣿⣿⣿⣿⣿⣿⢿⣩⡷⢂⣼⣿⣿⣿⣿⣿⣿⡟⠉⠋⠁⠈⢿⣿⠃⠀⠈⠙⢿⣿⣿⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠀⠀⢳⣀⠀⡀⢀⠀⣀⣠⣖⢺⣟⣛⢸⣿⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⢸⣿⣿⣧⠘⣿⣇⢀⠀⠁⠘⠐⠗⠾⠿⠿⠧⣼⣿⠇⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣠⣀⣀⣹⣷⡀⠀⠀⠀⠀⢻⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠐⣍⣧⣽⣬⣧⣼⣿⣿⣿⣿⣿⡿⠟⠀⡛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⢃⣸⣿⣿⣿⣧⠸⣿⣿⣤⣀⣆⠠⢠⠤⠤⣤⣶⣼⡟⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⡹⠋⠉⠽⠿⣿⣿⡄⠺⠣⠀⣾⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠹⣾⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⣠⡞⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠘⣸⣿⣿⣿⣿⣿⣆⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢉⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡁⠀⠀⠀⠀⠈⠙⠃⠀⣇⡐⠃⣼⣿⣿⣿⣿⢿⣷⣦⣍⣻⡛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡯⣝⣿⣿⣷⣶⣶⠛⣿⣿⣧⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣟⣻⣟⠛⠛⠿⡇
⢰⣿⣿⣿⣿⣿⣿⣿⣷⠀⢩⣟⡛⠿⠿⠛⢉⣠⡔⠒⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡄⢠⠀⠀⠀⠀⢸⠟⠉⠈⣿⣿⣿⣿⠇⣘⣻⣻⣿⢻⣿⣷⡿⠿⡛⢿⣟⣿⣿⣿⡿⣛⣻⣿⡇⠉⠀⠀⠉⠁⢠⣿⡏⢹⣿⣷⣾⣿⣍⢻⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣷⡆
⢨⣭⣉⣿⡿⠟⠋⠐⠺⠂⣿⣤⣏⢙⣿⣿⣿⠛⠃⠀⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠁⠈⠀⠀⠀⢠⡾⢶⠋⡀⢹⣿⣿⣏⣿⣿⣿⣿⣿⣉⡁⠹⣿⡌⣿⣿⡿⠉⠉⠀⣀⣀⡀⠈⠁⠨⠀⠀⠀⠀⠊⠙⢃⠈⠍⠉⣿⣿⡿⠟⠛⠛⠛⢉⣉⣭⣿⣿⣿⡆⢉⠉⠁⡄
⠈⠻⢿⣟⠁⠀⠀⠀⠀⠒⠈⠙⠻⠿⣿⣿⣿⠏⠉⠉⠑⢶⣦⡉⢻⣿⣿⣿⣿⡿⠿⠿⣿⣿⡀⠀⠀⠃⢀⣾⡏⠉⠙⠀⠈⣿⣿⣇⣹⣿⣿⣿⣿⣏⠀⠂⢸⣿⣿⣼⠀⠀⠀⠀⠀⠠⠄⠀⠀⠀⣀⣀⣀⡀⠂⢀⣩⣴⣶⠿⠛⠉⠀⢠⣤⡄⠯⣾⣿⣿⣿⣿⣿⠇⠀⠻⠀⠀
⠀⠀⣀⠙⣿⣶⣤⣀⡈⢀⣿⣿⣶⣶⣤⣴⣾⠀⠀⠀⠀⠀⣻⣿⣤⣿⣷⣶⣿⣿⣿⣷⣷⣦⣥⠆⣠⣾⣿⠟⠓⠀⠀⡀⠀⠈⠍⠛⢉⣿⣿⣿⣿⣿⡆⠀⣶⡻⣿⡿⠙⢻⣿⣶⣿⣶⣶⣶⣤⣾⣿⣿⣿⣿⣿⠿⠛⡉⠀⠀⠀⠊⢀⣼⣿⠻⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⡀⠀
⢀⠀⢻⣇⠙⣽⠛⠿⢿⣾⣿⣿⣿⣿⣿⡏⢀⣤⣴⣾⣿⣿⣿⣿⣿⡛⠋⠉⠉⠉⠉⠛⣿⣿⣿⡁⢈⠉⢁⣀⠀⠀⠘⠒⢂⡀⠄⠉⢹⣿⠿⠟⠛⠁⠀⠀⢻⣷⡆⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⠹⠿⠿⠛⠉⠀⠐⠋⠡⠀⡀⠀⣠⣾⡟⢻⣷⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠁⠀
⠀⠀⠈⠛⣷⣤⣀⡀⣾⣿⣿⣿⣿⣿⣿⣧⠸⡿⠟⠛⠉⠁⢠⣿⣿⠃⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⠈⣿⣿⡷⠉⢙⣩⠅⢠⣤⣤⣿⣿⠆⣠⠀⠀⡀⠀⠀⠹⣷⡀⠙⢿⣿⣿⣿⣿⣿⠏⢁⡀⠀⠀⠀⠀⠀⠀⢀⣐⣉⣴⣾⣿⠟⠀⠀⣿⣿⣧⣿⣿⣿⣫⠟⢻⣷⠀⠀⡀
⠀⠀⠀⠀⢌⠙⠻⣿⡏⠁⣀⠀⠙⠛⠋⠁⠀⠀⠀⢀⣠⣴⣿⣿⠃⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣃⣀⣀⠙⠟⢀⣀⡀⠀⣀⡸⢿⣿⣿⠇⣼⣷⣇⣰⠀⠀⠀⠀⠻⢷⡀⠈⢿⣿⠛⠛⠁⢠⣾⣿⣿⣿⡿⠻⡿⠿⠟⠛⣉⠙⢉⣀⣀⠀⢸⣿⡗⢸⣿⣿⡿⠃⡄⣿⣿⣇⠈⠁
⢸⣦⣀⠀⠀⠀⠀⠈⣷⣿⣿⣿⣷⣦⢿⣿⣶⡿⠿⠟⠛⠋⠉⢳⣧⠀⠀⠀⡠⠖⠋⣿⡿⣿⣿⠈⢍⠻⣿⠇⠘⠀⠈⠉⠀⢠⣾⣿⡏⠀⣿⣿⡿⢿⣀⡀⠀⣀⣠⣤⣧⣤⡀⠀⠀⠀⠐⠟⠛⠉⠁⠀⠀⠀⠂⠘⠓⠚⢁⠔⠀⠀⠈⢁⣼⣿⠟⡿⣿⡏⢀⣾⣇⢸⣿⣿⡄⠀
⠈⢿⠿⢿⣦⣤⡀⠺⠛⠿⢿⣿⡿⠋⠀⣀⠘⠉⠀⠀⠀⠀⠀⣸⣿⠀⢀⠎⣠⣾⢰⣿⡽⣿⣿⠀⠤⠠⣤⡆⠀⠲⠶⢶⣶⣾⣿⣿⣥⣞⡁⢹⣷⣈⣿⣷⣿⣿⣿⣿⣿⣿⣿⣷⣶⡦⠀⢠⡶⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠐⢃⣸⣶⣿⣿⣯⡿⣱⣿⡇⢼⣿⣿⢸⣿⣿⡷⠀
⠐⠢⠀⠀⠉⠉⠛⣷⣦⣄⣸⣥⣀⣠⣦⣤⣤⣤⣤⣶⣦⣾⣿⡿⠃⢀⡌⢰⣿⡿⢸⣿⡇⣿⣿⣇⣀⣀⠈⠉⠀⣀⡀⠀⢠⣿⣿⡏⢨⢹⣷⢸⣿⣿⡌⠙⠿⠿⢿⣿⣏⣿⣿⣿⣧⠀⡆⢸⣿⣄⠀⠀⠀⠀⠈⢓⣀⣤⣴⣾⣿⣿⡿⣿⠟⠁⠀⢹⣿⣿⡌⣿⣿⢸⣿⣿⡇⡄
        ''')  # <<< ASCII Art 1 in RED
    elif banner_choice == 2:
        print(Fore.GREEN + ''' 
                                  ⠀⢀⡀⣀⣴⡯⠖⣓⣶⣶⡶⠶⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⢀⣴⣯⡾⣻⠽⡾⠽⠛⠚⠷⠯⠥⠤⠤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣢⣾⢿⣶⠿⣻⠿⠿⢋⣁⣠⠤⣶⢶⡆⠀⣀⣀⣀⣀⣀⣐⡻⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠟⠛⠉⠪⠟⣩⠖⠋⢀⡴⢚⣭⠾⠟⠋⡹⣾⠀⠀⢀⣠⠤⠤⠬⠉⠛⠿⣷⡽⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⣿⢝⣯⠆⣩⠖⢀⣤⢞⣁⣄⣴⣫⡴⠛⠁⠀⡀⣼⠀⣿⢠⡴⠚⠋⠉⠭⠿⣷⣦⡤⢬⣝⣲⣌⡙⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣷⣿⣿⣾⣿⣷⣿⣿⣿⣿⠋⠀⢀⢀⣶⣷⣿⠀⣿⠀⠀⠀⠀⠀⠀⠐⠚⠻⣿⣶⣮⣛⢯⡙⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣸⣿⠋⠀⡆⣾⣾⣿⣿⠿⢂⣿⣄⠀⠀⠀⠀⠀⠀⠐⠢⢤⣉⢳⣍⠲⣮⣳⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠿⣷⡀⢸⣿⣿⣿⠙⠏⠁⣸⣿⣿⣭⣉⡁⠀⠀⠀⠀⠀⠀⠘⣿⣿⡷⣌⣿⡟⢿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡿⡏⢡⢟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⣷⣼⣿⡟⠋⠀⠀⣴⣿⣿⣦⣍⣙⣓⡦⠄⠀⠈⠙⠲⢦⣻⣿⡅⠘⣾⣿⡄⠹⡳⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢹⠀⠀⠞⢭⣻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⠳⢼⣧⣄⣠⣾⣿⣿⣿⡻⢿⣭⡉⠁⠀⠀⠀⠀⠀⠀⠙⢿⢻⡄⠈⢻⣿⠀⠉⠹⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣻⡇⡆⠀⢀⣶⣾⣳⠏⠉⢹⡿⣿⣿⣟⡿⠿⢿⣿⣿⣿⣿⣧⠘⠒⠮⣿⣿⣿⣿⣿⣿⣿⣦⡬⠉⠀⠀⠀⢦⠀⠰⡀⠀⠈⠃⠓⠀⠈⣿⡀⠀⠀⢹⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣾⡧⣔⠾⡏⠙⠁⠀⣠⣿⢀⡎⠉⠈⠻⠭⠤⠤⣌⡻⣿⡿⡀⠈⠙⠻⠿⠿⣯⣅⠉⠉⣝⠛⢦⡘⣶⡀⠀⢣⠀⠙⢦⡀⠘⢇⣆⠀⣿⡇⠀⠀⠀⡇
⠀⠀⠀⠀⠀⣀⡠⠶⠿⠟⣃⣀⡀⠀⠀⠈⢓⣶⣾⣟⡡⠞⠀⠀⠀⠠⠴⠶⠿⠷⢿⡼⣿⣗⠀⠀⠀⠀⠀⠀⠈⠛⢆⠈⢧⡀⠁⠘⣿⡄⢢⠇⠀⠈⢧⠀⠸⣼⡄⣿⠇⠀⠀⢧⢸
⠀⣠⠴⠾⣿⡛⠛⠛⠁⠀⠀⠀⠙⠲⠈⠉⠀⠀⠀⠀⠤⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠘⢿⠷⣄⠘⣷⣄⡀⡄⠀⢀⡀⠀⢳⡄⠀⠀⠳⠀⡏⠀⠀⠸⡄⠀⢿⣧⣿⠀⠀⠀⡀⣼
⣾⣿⢶⣦⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⣤⣶⣶⣒⠢⢤⠀⠀⠈⠁⠉⠛⠿⣎⡛⢦⣀⠈⣿⣴⣾⣿⡞⡄⠀⠀⢹⡀⠀⠀⣿⠀⣾⣿⠇⠀⠀⠀⡇⢸
⠘⣿⣿⡾⡇⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡐⠲⢦⣦⢤⣤⣤⡶⠛⠉⠉⠀⠀⠀⠀⢀⣠⣤⣀⣤⠴⠂⠀⠀⠁⠀⢹⣧⣿⡿⢸⠇⢻⣿⣆⠀⠀⢷⣀⠀⣿⣷⠟⠉⠀⠀⠀⢸⡇⡄
⠀⠈⠳⢭⡗⠒⣛⣻⣽⠿⢿⣯⣷⣾⣿⣿⣿⣶⣬⡉⣉⠈⠑⠒⠉⠙⠻⠯⠉⣩⡟⢁⣾⠏⠀⣾⣷⣤⣄⣀⡀⢨⡿⣿⡇⣸⠀⠘⡿⢹⣆⠀⣸⣿⣷⡿⠁⠀⡀⠀⢸⡀⣾⣧⠀
⠀⠀⠀⠀⠈⠻⠿⣿⢿⡷⣌⣣⡉⠛⢿⣿⣿⣿⣿⣿⣧⡓⢄⠀⠀⠀⠀⠀⢰⡿⠷⣟⠿⠋⠀⢹⣿⡇⠀⠁⠙⣾⢧⠙⠙⠁⠀⠐⠁⠘⠹⣄⣿⠃⠹⣿⡀⠀⡇⠀⡿⣇⡿⢹⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠓⠻⠊⠙⠃⠀⠀⠹⣿⣿⡿⡏⠀⣿⣌⠳⡄⠀⢀⡴⠋⠈⠉⠉⡙⠲⣤⢸⡟⣿⠀⠀⠠⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠿⠃⠀⠀⠈⠃⣸⡇⣼⠇⣿⡇⢸⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⢳⣿⣿⣿⡆⢳⠀⡎⠀⠀⠀⠀⢀⣉⠳⣬⣿⠇⠃⠀⠀⢠⠆⢰⢊⡇⠀⠀⠀⠀⠀⠀⢲⠀⢰⡆⠀⠀⣽⣿⡟⠀⢸⡇⡞⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢸⡇⠈⣿⢟⣼⣇⡏⠀⠀⠔⣺⡭⠽⣿⡛⠛⠿⡏⠀⣆⠀⠀⣼⠀⣼⣼⣷⡆⠀⠀⣶⡆⢠⡿⣠⣿⡇⠀⢰⣿⠏⣴⢂⠋⡼⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡆⢻⢿⡁⣼⢣⣿⡿⠀⢀⢀⡴⠋⠀⠀⠀⠀⠙⣶⣦⡅⠀⣿⡄⢠⣿⣾⢿⠿⣿⡇⠀⠘⣾⣇⣼⣷⠟⡼⠀⣰⡿⠋⢠⠏⢦⣾⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡟⢾⢄⣹⣧⡿⡽⠁⠀⣿⠋⠀⠀⠀⠀⠀⠀⠀⠟⠉⣧⡾⡽⣠⣿⢛⠇⠏⠰⣻⠃⣼⣽⣿⡿⡿⠁⣴⣡⡾⠋⠀⢠⣞⣴⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣼⣿⣿⡟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠋⠰⠟⣻⣿⢋⠀⠀⣴⣷⣾⠟⡿⠋⠀⣥⠾⠛⡋⠀⠀⢠⣾⣿⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠽⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢁⡌⠀⢰⣿⠟⠁⠀⠀⠀⠀⡀⠀⣰⠃⠀⣴⡿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⢀⣴⠏⠀⠀⢸⡋⠀⡀⠀⣀⠖⠋⣠⣾⢃⣠⡾⠟⢡⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⣀⣴⡿⠃⠀⠀⠀⠀⢁⡾⠁⢈⣁⣴⣾⣿⣿⠟⠉⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣾⣿⡿⠁⠀⢀⣀⣤⣼⢟⣡⣶⠿⠟⠋⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣟⣿⣿⣃⣴⣶⣿⠿⣿⣿⡿⠋⠀⠀⠀⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣾⣿⣿⣿⠛⠉⠀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠟⠁⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⠀⠀⠀⠀⠀
        ''')  # <<< ASCII Art 2 in GREEN
    elif banner_choice == 3:
        print(Fore.BLUE + ''' 
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀
⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
⠀⠀⢸⣿⣿⠟⣋⡉⠉⠉⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠉⠉⣉⡛⢿⣿⣿⡄⠀
⠀⠀⣾⣿⣷⣾⣿⣷⣦⣌⡑⠠⡀⠀⢹⣿⣿⣿⣿⠋⠀⡀⠐⣉⣤⣴⣾⣿⣷⣽⣿⡇⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠲⣼⣿⣿⣿⣿⡶⠊⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠀⣿⣿⣿⡿⠛⠛⠉⠛⠛⠿⣿⡄⠘⣿⣿⣿⣿⣡⣾⣿⠟⠛⠉⠙⠛⠻⢿⣿⣿⡇⠀
⠀⠀⣿⣟⠉⠀⠀⠀⠀⠀⠀⠀⣈⡇⠀⢹⣿⣿⣿⣿⣏⡀⣀⣀⣀⣀⣀⣀⣀⣙⣛⡇⠀
⠀⠀⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠀⢀⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀
⠀⠀⠘⣆⠈⠛⢛⣛⣛⣛⣿⠉⢀⡀⠀⣾⣿⣿⣿⣷⣍⢻⣿⣛⠿⠿⠿⠿⠛⢉⡆⠀⠀
⠀⠀⠀⠹⣆⢳⡀⠻⣿⣿⣿⣦⣼⡇⢀⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡿⠁⣰⢃⣾⠀⠀⠀
⠀⠀⠀⠀⠻⣧⡱⡄⠈⠙⠻⠿⠿⠟⠈⠻⠿⠟⠋⠻⣿⣿⡿⠿⠋⢀⣼⢋⣼⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣷⡈⠳⣤⣀⡀⠀⠀⠀⣠⣶⣄⠀⠀⠀⠀⠀⣀⣴⡞⢁⣾⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⡄⠈⠻⢿⣿⣷⣶⣿⣭⣭⣶⣶⣶⣾⣿⣿⡿⣡⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⢸⣿⣿⣭⣟⠛⠛⠛⢛⣿⣿⣿⣿⡟⣵⡟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡌⣿⣿⣿⣿⠆⠀⠀⣿⣿⣿⣿⣟⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣿⣿⣿⡟⠀⠀⠀⢻⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣷⠀⠀⠀⣼⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡄⠀⢀⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')  # <<< ASCII Art 3 in BLUE
    elif banner_choice == 4:
        print(Fore.MAGENTA + ''' 
       ⣀⣤⣴⣶⣶⣶⣿⣿⣿⣷⣶⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡏⠉⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠉⣿⣿
⢻⣿⡇⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⢀⣿⡇
⠘⣿⣷⡀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⠿⠛⠋⠀⠀⠀⠀⠀⠀⢀⣼⣿⠃
⠀⠹⣿⣿⣶⣦⣤⣀⣀⣀⣀⣀⣤⣶⠟⡿⣷⣦⣄⣀⣀⣀⣠⣤⣤⣶⣿⣿⡟⠀
⠀⠀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
⠀⢈⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣷⠀⣼⣷⠀⣸⣿⣿⣿⡿⠿⠿⠿⣿⣿⣿⡇⠀
⠀⠘⣿⣿⣿⡟⠋⠀⠀⠰⣿⣿⣿⣷⣿⣿⣷⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⠟⠁⠀
⠀⠀⠈⠉⠀⠈⠁⠀⠀⠘⣿⣿⢿⣿⣿⢻⣿⡏⣻⣿⣿⠃⠀⠀⠀⠈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣿⢸⣿⡇⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣿⢸⣿⡇⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣿⣿⢸⣿⡇⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣿⣿⢸⣿⠃⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡇⣿⣿⢸⣿⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠇⢿⡿⢸⡿⠀⠿⠟
        ''')  # <<< ASCII Art 4 in MAGENTA
    else:
        print(Fore.YELLOW + "Invalid choice. Please choose 1, 2, 3, or 4.")
    
if __name__ == "__main__":
    print(Fore.CYAN + "Choose a banner to display:")
    print(Fore.CYAN + "1. Banner 1")
    print(Fore.CYAN + "2. Banner 2")
    print(Fore.CYAN + "3. Banner 3")
    print(Fore.CYAN + "4. Banner 4")
    choice = int(input(Fore.CYAN + "Enter the number of your choice: "))
    show_banner(choice)