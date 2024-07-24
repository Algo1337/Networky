import os, importlib, discord

from discord import message

DEFAULT_MESSAGE_MODERATOR = "__events__"

"""
    Example Tree Of the Command Directory 

    - __events__ Directory is ignored while scanning for commands!

    - __events__/
        | - on_message_event.py
        | - on_join_event.py
        | - on_vc_event.py
    - help_cmds/
        | - help.py
        | - server.py
        | - tools.py
    - tools/
        | - geo.py
        | - pscan.py
"""

class DiscordCogs():
    
    cmd_paths:  list[str] = [];
    commands:   dict[str] = {};
    def __init__(self, cmd_dir: str):
        self.dir = cmd_dir;
        self.module_link = self.dir.replace("/", ".").replace("\\", ".")
    
        self._loadCmds();

        if not self.LoadMessageModerator():
            print("[ x ] No message_watch found....!")

    def _loadCmds(self, path: str = "") -> None:
        i = 0

        root_dir = os.listdir(self.dir)
        total_count = len(root_dir)
        for item in root_dir:
            if item == "__pycache__" or item == DEFAULT_MESSAGE_MODERATOR: continue
            if os.path.isdir(self.dir + item):
                next_dir = os.listdir(self.dir + item)
                total_count += len(next_dir)
                for nitem in next_dir:
                    if nitem == "__pycache__": continue
                    print(f"[ NEW ] [DIR] {i}/{total_count} {self.dir}{item}/{nitem} | Module Link: {self.module_link}{item}.{nitem}")
                    self.commands[f'{nitem.replace(".py", "")}'] = Library(f'{self.module_link}{item}.{nitem.replace(".py", "")}')

                    i += 1
                continue

            
            if not os.path.isdir(item):
                print(f"[ NEW ] [ROOT]  {i}/{total_count} {self.dir}{item} | Module Link: {self.module_link}{item}")
                self.commands[item.replace(".py", "")] = Library(f'{self.module_link}{item.replace(".py", "")}')
            
            i += 1

    """
        User must have 'on_msg_event.py' in the moderation directory within the command dir
    """
    def LoadMessageModerator(self) -> bool:
        if not os.path.exists(f'{self.dir}modertion/on_msg_event.py'):
            return False; 
    
        self.commands["on_msg_event"] = Library(f'{self.module_link}moderation.on_msg_event')
        return True
    
    """
        User must have 'on_vc_event.py' in the moderation directory within the command dir
    """
    def LoadVCModeration(self) -> bool:
        if not os.path.exists(f'{self.dir}moderation/on_vc_event.py'):
            return False
        
        self.commands["on_vc_event"] = Library(f'{self.module_link}moderation.on_vc_event')
        return True

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