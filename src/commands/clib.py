import discord, os

from ..utils.discord.messages import *

class clibEngine:
        headers:        dict[str, str] = {}
        def __init__(self) -> None:
                files = os.listdir("headers/")
                for file in files:
                        self.headers[file] = self.__readFile(file)

                # print("[ + ] All headers loaded....!")

        def SearchQuery(self, q: str) -> str:
                self.query = q
                results = ""
                for header in self.headers:
                        if q in self.headers[header]:
                                results += self.get_query_from_file(self.headers[header])

                return results

        def get_query_from_file(self, file_data: str) -> str:
                results = ""
                lines = file_data.split("\n")
                i = 0
                for line in lines:
                        if self.query in line:
                                results = "\n".join(lines[i - 4:i + 1])
                                return results
                        i += 1

                return results

        def __readFile(self, filename: str) -> str:
                file = open(f"headers/{filename}", "r+")
                data = file.read()
                file.close()
                return data;

async def clib(message: discord.message) -> bool:
    msg = Message(message)

    if len(msg.args) != 2:
        return await Message.SendEmbedMsg(message, "clib+ Page", "Error, Invalid arguments!", {})
    
    eng = clibEngine()

    search = eng.SearchQuery(msg.args[1]);

    if not eng:
        return await Message.SendEmbedMsg(message, "clib+ Page", "No matches found...!", {})
    
    await Message.SendEmbedMsg(message, "clib+ Page", f"```c\n{search}```", {});
    return True
