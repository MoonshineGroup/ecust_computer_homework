import zipfile
import os
import openpyxl
from docx import Document
import shutil

def mkdir():
    clean()
    if not os.path.exists("./answer"):
        os.makedirs("./answer")
    else:
        shutil.rmtree("./answer")
        os.makedirs("./answer")
        for i in range(1,7):
            os.makedirs("./answer/%d"%i)
        os.rmdir("./answer/3")
        os.rmdir("./answer/4")
def extract():
    fname="bundle.zip"
    with zipfile.ZipFile(fname) as zf:
        zf.extractall()
def clean():
    fname="bundle"
    if os.path.exists(fname):
        shutil.rmtree(fname)
    
def addInfoToMSOfficeFile(u_info,path:str):
    if path.endswith(".xlsx"):
        wb = openpyxl.load_workbook(path)
        wb.properties.lastModifiedBy = u_info["name"]
        wb.save("./answer/6/%s.xlsx"%u_info["id"])
    elif path.endswith(".docx"):
        docxfile = Document(path)
        docxfile.core_properties.last_modified_by = u_info["name"]
        docxfile.save("./answer/5/%s.docx"%u_info["id"])
    os.remove(path)

def modifyProgram2(u_info):
    fname="./bundle/2/2.py"
    with open(fname,mode="r+",encoding="utf-8") as f:
        lines = f.readlines()
    lines[0] = "info='%s%s'\n"%(u_info["name"],u_info["id"])
    with open("./answer/2/2.py","w",encoding="utf-8") as f:
        f.writelines(lines)

if __name__=="__main__":
    try:
        u_name=input("Enter your name: ")
        u_id=input("Enter your id: ")
        u_info={"name":u_name,"id":u_id}
        print("Extracting files...",end="")
        mkdir()
        extract()
        
        shutil.copyfile("./bundle/1/1.py","./answer/1/1.py")
        shutil.copytree("./bundle/3","./answer/3")
        shutil.copytree("./bundle/4","./answer/4")
        modifyProgram2(u_info)
        addInfoToMSOfficeFile(u_info,"./bundle/5/5.docx")
        addInfoToMSOfficeFile(u_info,"./bundle/6/6.xlsx")
        print("OK.")
        print("Refering answers saved to here.")
        clean()
    except Exception as e:
        print("Error occured: %s"%e)
        clean()