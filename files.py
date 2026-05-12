from pathlib import Path
import shutil

def sort_directories(src_str: str, dst_str: str):
    src = Path(src_str)
    dst = Path(dst_str)
    for item in src.iterdir():
        if item.is_dir():
            sort_directories(item, dst)
        else:
            try:
                suffix = item.suffix[1:]
                (dst / suffix).mkdir(parents=True, exist_ok=True)
                shutil.copy(item, (dst/suffix))
            except Exception as e:
                print(f"Failed to access the directory: {src}") 


if __name__ == "__main__":
    input_str = input("Please, provide source and optionally destination folders: ")
    input_split = input_str.split(" ")
    if len(input_split) > 1:
        src_dir, dst_dir = input_str.split(" ")
    else:
        src_dir = input_str.split(" ")[0]
        dst_dir = "dist"
    sort_directories(src_dir, dst_dir)