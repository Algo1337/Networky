
def parse_shit_html_bs(line: str) -> str:
    if "break-all" not in line and "break-word" not in line:
        return ""
    
    new = line.replace("</td>", "").replace("<strong>", "").replace("</strong>", "")
    ignore = True
    new_str = ""
    for ch in new:
        if ch == ">" and ignore:
            ignore = False
            continue

        if not ignore:
            new_str += ch

    return new_str