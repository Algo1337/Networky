from .cogs import *

## Temporary Config Settings
class Config:
    prefix = "+"

    @staticmethod
    def load_all_cogs() -> None:
        cmds = {}
        files = os.listdir("src/commands/")
        if len(files) == 0:
            return cmds

        i = 1
        for file in files:
            if file.endswith(".py"):
                print(f'[ + ] Command {i}/{len(files)-1}: {file.replace(".py", "")} Loaded....')
                cmds[file.replace(".py", "")] = Library(f'src.commands.{file.replace(".py", "")}')
            i+=1

        return cmds