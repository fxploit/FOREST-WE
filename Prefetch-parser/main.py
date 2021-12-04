import os
import sys
from argparse import ArgumentParser
from windowsprefetch import Prefetch

def main():

    args = "C:\\Users\wnstn\Documents\Parser\Windows-Prefetch-Parser-master\TestFiles\Win10"  #수집된 프리패치 폴더 경로
    file_paths = []
    if os.path.isdir(args): # isdir()해당 디렉토리 확인
        for filename in os.listdir(args): # listdir()는 인자로 넘겨준 경로의 파일 리스트를 리턴
            file_paths.append(os.path.join(args, filename))
    else:
        file_paths.append(args)

    parsed_files = []
    for filepath in file_paths:
        if filepath.endswith(".pf"):
            if os.path.getsize(filepath) > 0:
                p = Prefetch(filepath)
                parsed_files.append(p)
                p.prettyPrint()


if __name__ == '__main__':
    main()