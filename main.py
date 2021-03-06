import os
import sys
from urllib import request
from wavdraw import *
from wavsave import *
from wavresample import *
from utils import *
from curl import *
from voice import *


def usage():
    print("The HMM/DNN-Based Singing Voice Syntheis System \"SinsyPlus\"")
    print("Version 0.0.1 (https://github.com/740291272/SinsyPlus)")
    print("Copyright (C)2009-2018 Nagoya Institute of Technology")
    print("Copyright (C)2017-2018 GloomyGhost")
    print("All rights reserved")
    print()
    print("Usage:")
    print("\tSinsyPlus [infile] [Language]")
    print("\t\tLanguage:")
    print("\t\t\tJapanese:ja")
    print("\t\t\tChinese :ch")
    print("\t\t\tEnglish :en")
    print("\tExample : sinsyplus voice.xml ja ")
    os.system('pause')



# 程序入口
if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        XML = sys.argv[1] # 读取XML
        if len(sys.argv) < 3:
            lang = lang()  # 读取语言
        else:
            lang = langnum(sys.argv[2])
        langstr = langstr(lang)  # 获取语言
        print(langstr)
        print("Upload MusicXML...")
        fileName = text(curl(lang, langstr, XML))  # 获取文件名
        print("Synthesising from servers...")
        req = request.Request('http://sinsy.sp.nitech.ac.jp/temp/'+ fileName + ".wav")
        link = "http://sinsy.sp.nitech.ac.jp/temp/"+ fileName + ".wav"
        # Save Wav
        fileNameSave = fileName + ".wav"
        download(link, fileNameSave)
        # draw wav
        wavedraw(fileNameSave)
