import os

def bulk_rename(files,ext):
    file_with_ext = [f for f in files if f.endswith(ext)]
    print(file_with_ext)
    for i,file in enumerate(file_with_ext):
         new_name = f"image_{i+1}{ext}"
         os.rename(file,new_name)
         print(f"Renamed: {file} to {new_name}")

if __name__ == "__main__":
    all_files = os.listdir()
    bulk_rename(all_files,".jpg")