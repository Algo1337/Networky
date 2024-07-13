import os, importlib, discord

from discord import message

class DiscordCogs():
    cmd_paths:  list[str] = [];
    commands:   dict[str] = {};
    def __init__(self, cmd_dir: str):
        self.dir = cmd_dir;
    
        self._loadCmds();

    def _loadCmds(self, path: str = "") -> None:
        i = 0

        current_dir = self.dir
        module_link = self.dir.replace("/", ".").replace("\\", ".")

        root_dir = os.listdir(current_dir)
        for item in root_dir:
            if item == "__pycache__": continue
            if os.path.isdir(current_dir + item):
                next_dir = os.listdir(current_dir + item)
                for nitem in next_dir:
                    if nitem == "__pycache__": continue
                    print(f"[ NEW ] [DIR] {current_dir}{item}/{nitem} | Module Link: {module_link}{item}.{nitem}")
                    # print(f"[ + ] [NEW] Command: {item}/{nitem.replace(".py", "")} Loaded....")
                    self.commands[f'{nitem.replace(".py", "")}'] = Library(f'{module_link}{item}.{nitem.replace(".py", "")}')
                continue

            
            if not os.path.isdir(item):
                print(f"[ NEW ] [ROOT] {current_dir}{item} | Module Link: {module_link}{item}")
                # print(f"[ + ] [NEW] Command: {item.replace(".py", "")} Loaded....")
                self.commands[item.replace(".py", "")] = Library(f'{module_link}{item.replace(".py", "")}')

            
    """
        User must have 'message_watch.py' in the command root directory
    """
    def LoadMessageModerator(self) -> bool:
        if not os.path.exists(f'{self.dir}message_watch.py'):
            return False; 
    
        self.commands["message_watch"] = Library(f'{self.dir}message_watch')

    """
        Search for cmd and execute if found like cogs do for you alrdy

        cmd_exec = cmd.ExcuteCmd(args[0])
        if not cmd_exec:
            await message.channel.send("[ X ] Command was not found!")
    """
    async def ExecuteCmd(self, cmd_used: str, message: discord.message) -> bool:
        if cmd_used in self.commands:
            await self.commands[cmd_used].execute_method(cmd_used, message)
            return True
            
        return False

class Library:
    lib:        None;
    path:       str = "";
    vars:       list = [];
    methods:    list = [];
    def __init__(self, lpath: str) -> None:
        if not os.path.exists(lpath.replace(".", "/") + ".py"):
            print("ERROR, MISSING LIB " + self.path);
            return
        
        self.path = lpath;
        self._loadLib();

    def _loadLib(self) -> None:
        self.lib = importlib.import_module(self.path.replace("/", "."))
        if not hasattr(self, "lib"):
            print("ERROR, MISSING LIB " + self.path);
            return False;
        
        lib_content = open(self.path.replace(".", "/") + ".py", "r").read();

        for line in lib_content.split("\n"):
            if line.startswith("def"):
                self.methods.append(self.__get_method_name(line));
    
    def retrieve_method(self, method_name: str):
        if not hasattr(self.lib, method_name):
            return None;
        
        return getattr(self.lib, method_name);

    """ Specific method for Discord.PY ONLY """
    async def execute_method(self, method_name: str, discord_var) -> bool:
        if not hasattr(self, "lib"):
            print("ERROR, MISSING LIB " + self.path);
            return False;
        
        if not hasattr(self.lib, method_name):
            print("ERROR, MISSING METHOD");
            return False;
        
        method = getattr(self.lib, method_name);
        await method(discord_var);
        return True;
                
    def __get_method_name(self, line: str) -> str:
        name = "";
        for chr in line.split(" ")[1]:
            if chr == "(":
                break;

            name += chr;

        return name;


# DiscordCogs("src/commands/")