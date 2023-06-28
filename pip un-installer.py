import subprocess
import sys
import time
import random


def animate_cover():
    sys.stdout.write("""
████████╗███████╗███╗   ███╗██████╗ ███████╗██╗   ██╗
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔════╝╚██╗ ██╔╝
   ██║   █████╗  ██╔████╔██║██████╔╝█████╗   ╚████╔╝
   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══╝    ╚██╔╝
   ██║   ███████╗██║ ╚═╝ ██║██║     ██║        ██║
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝        ╚═╝
    """)
    sys.stdout.write("\n")
    sys.stdout.write("un/installer for pips")
    sys.stdout.write("\n")
    sys.stdout.write("Loading")
    start_time = time.time()
    stop_time = start_time + random.uniform(5, 10)

    while time.time() < stop_time:
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write("\b \b" * 3)
        sys.stdout.flush()
        time.sleep(0.5)

    sys.stdout.write("\r")
    sys.stdout.write(" " * 13)
    sys.stdout.write("\r")
    sys.stdout.flush()
    time.sleep(1.5)  # 1.5 seconds pause


def install_packages():
    package_names = input("Which packages do you want to install? (comma-separated) ")
    package_list = package_names.split(",")
    count = 0

    for package in package_list:
        subprocess.call(['pip', 'install', package])
        count += 1

    print(f"{count} packages were installed: {', '.join(package_list)}")


def uninstall_packages(show_packages_list):
    if show_packages_list:
        list_installed_packages()
    package_names = input("Which packages do you want to uninstall? (comma-separated) ")
    package_list = package_names.split(",")
    count = 0

    for package in package_list:
        subprocess.call(['pip', 'uninstall', package, '-y'])
        count += 1

    print(f"{count} packages were uninstalled: {', '.join(package_list)}")


def list_installed_packages():
    output = subprocess.check_output(['pip', 'freeze'])
    installed_packages = output.decode('utf-8').strip().split('\n')
    print("The following packages are installed:")
    for package in installed_packages:
        print(package)
    print()


def main():
    animate_cover()
    show_packages_list = True
    list_installed_packages()

    install_or_uninstall = input("Do you want to install or uninstall packages? (i/u) ")
    if install_or_uninstall.lower() == 'i':
        install_packages()
    elif install_or_uninstall.lower() == 'u':
        uninstall_packages(show_packages_list=False)

    input("Press enter to exit the program.")


if __name__ == '__main__':
    main()