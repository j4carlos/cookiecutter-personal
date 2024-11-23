import subprocess

MESSAGE_COLOR = "\x1b[34m"
W_COLOR = "\x1b[38;5;40m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git','init'])
subprocess.call(['git','add','*'])
subprocess.call(['git','commit','-m','Initial commit'])

print(f"{MESSAGE_COLOR}The beginnig of your destiny is defined now! Create and have fun! {RESET_ALL}")

print(f"{W_COLOR}Bye, hello{RESET_ALL}")
