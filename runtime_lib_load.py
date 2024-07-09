import os, importlib

class Library:
    lib:        None;
    path:       str = "";
    vars:       list = [];
    methods:    list = [];
    def __init__(self, lpath: str) -> None:
        if not os.path.exists(lpath + ".py"):
            return
        
        self.path = lpath;
        self._loadLib()

    def _loadLib(self) -> None:
        self.lib = importlib.import_module(self.path)
        print(dir(self.lib))
        lib_content = open(self.path + ".py", "r").read();

        for line in lib_content.split("\n"):
            if line.startswith("def"):
                print(f"Function Found: {self.__get_method_name(line)}")
                self.methods.append(self.__get_method_name(line));
    
    def retrieve_method(self, method_name: str):
        if not hasattr(self.lib, method_name):
            return None
        
        return getattr(self.lib, method_name);
                
    def __get_method_name(self, line: str) -> str:
        name = "";
        for chr in line.split(" ")[1]:
            if chr == "(":
                break

            name += chr

        return name;

gglib = Library("gg")
test = gglib.retrieve_method("test")
test()

def load_all_cogs() -> None:
    cmds = {}
    files = os.listdir("src/commands/")
    if len(files) == 0:
        return cmds

    for file in files:
        if file.endswith(".py"):
            cmds[file.replace(".py", "")] = Library(file.replace(".py", ""))

    return cmds