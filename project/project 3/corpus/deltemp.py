#this module clears temporary files

def deltempfiles():
        import os
        dirPath = r"C:\Windows\Prefetch"
        os.chmod(dirPath, 0777)
        fileList = os.listdir(dirPath)
        for fileName in fileList:
                try:
                        
                        os.remove(dirPath+"\\"+fileName)
                except:
                        pass
        
        print 'done'
        dirPath=r"C:\Windows\Temp"
        for fileName in fileList:
                try:
                        
                        os.remove(dirPath+"\\"+fileName)
                except:
                        pass
        

        dirPath=r"C:\Users\PARTHD~1\AppData\Local\Temp"
        for fileName in fileList:
                try:
                        
                        os.remove(dirPath+"\\"+fileName)
                except:
                        pass
        
                
