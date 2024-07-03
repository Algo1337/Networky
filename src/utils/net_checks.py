
def validate_ipv4_format(ip_addr: str) -> bool:
    if not ip_addr:
        return False;

    args = ip_addr.split(".")
    if len(args) != 4:
        return False
    
    if args[0] < 1 or args[0] > 255: return False;
    if args[1] < 0 or args[1] > 255: return False;
    if args[2] < 0 or args[2] > 255: return False;
    if args[3] < 0 or args[3] > 255: return False;

    return True;
