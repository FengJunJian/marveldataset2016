import os
import shutil
import codecs
import re

def countFiles(path='./'):
    count=0
    allfiles=[]
    walk=os.walk(path)
    for root,dirs,files in walk:
        rematch=re.match(r'.*W[0-9]_[0-9]', root)
        if rematch is None:
            continue

        print(rematch)
        print(root, len(files))
        count+=len(files)
        for file in files:
            #print(root,file)
            # count+=1
            allfiles.append(file)

    print('Count',count,len(allfiles),len(set(allfiles)))


def copyfiles2class(finalContent,path='./'):
    walk = os.walk(path)
    repectC=0
    copyC=0
    for root, dirs, files in walk:
        #alist = []
        rematch = re.match(r'.*W[0-9]_[0-9]', root)
        if rematch is None:
            continue
        # print(rematch)
        for file in files:

            _, ext = os.path.splitext(file)
            if ext != '.jpg':
                break
            name, ext = os.path.splitext(file)
            # print(name)
            classname = finalContent[name]
            if not os.path.exists(classname):
                os.makedirs(classname)
            src = os.path.join(root, file)
            dst = os.path.join(classname, file)
            if os.path.exists(dst):
                #print(dst)
                repectC+=1
            else:
                shutil.copyfile(src, dst)
                copyC+=1

    print('repect:',repectC)
    print('copyC:',copyC)


def judementClass(name_class,path='./'):#判断文件夹中的船舶图片是否属于同一类
    dirdict={}
    walk=os.walk(path)
    for root,dirs,files in walk:
        alist=[]

        for file in files:
            _,ext=os.path.splitext(file)
            if ext !='.jpg':
                break
            #basename=os.path.basename(file)
            name,ext=os.path.splitext(file)
            #print(name)
            alist.append(name_class[name])
        if len(alist)>0:
            dirdict.update({root:alist})
    for key in dirdict.keys():
        print(key,set(dirdict[key]))
    return dirdict

def findmore(allfiles):
    for i,f in enumerate(set(allfiles)):
        count=allfiles.count(f)
        if count>1:
            print(i,f,count)
    num=allfiles.index(f)
    index=[i for i,x in enumerate(allfiles) if x==allfiles[num]]
    print(index)
    return index



#pattern=r'!(W[0-9]_[0-9])'
#result=re.match(pattern,'dadfadW2_51')
FILE_TO_DOWNLOAD_FROM = "VesselClassification.dat"

downloadFile = codecs.open(FILE_TO_DOWNLOAD_FROM,"r","utf-8")
downloadContent = downloadFile.readlines()
downloadFile.close()

finalContent = {}#名字：类别
classname=set()
allfiles=[]
filesClass=[]
for index,eachLine in enumerate(downloadContent):
    strlist=eachLine.strip().split(',')
    fileName,fileClass = strlist[0],strlist[-1]
    if fileName in finalContent and finalContent[fileName] != fileClass:
        #:
        print('file:',fileName,fileClass)
        print('dict:',fileName,finalContent[fileName])

    else:
        finalContent.update({fileName: fileClass})

    allfiles.append(fileName)
    filesClass.append(fileClass)
    classname.add(fileClass)

print([len(classname),classname])
print(len(finalContent),len(allfiles))
copyfiles2class(finalContent,path='./')



count=0
for c in classname:
    files=os.listdir(c)
    print(c,len(files))
    count+=len(files)
print(count)













