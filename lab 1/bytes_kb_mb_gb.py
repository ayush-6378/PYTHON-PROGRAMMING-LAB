print("bytes to kb,mb,gb conversion")

def bytes_kb_mb_gb():
    bytes=int(input("how many bytes:"))
    kb=bytes/1024
    mb=kb/1024
    gb=mb/1024
    print(bytes,"bytes is equal to:", kb,"kb,", mb,"mb and", gb,"gb")

bytes_kb_mb_gb()