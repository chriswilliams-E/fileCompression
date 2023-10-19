#!/usr/bin/python3

import zlib

def deflateFiles(fileName):
    compzFile = open(fileName, 'rb').read()
    print('Deflating %s' % fileName)
    deflateData = zlib.compress(compzFile, zlib.Z_BEST_COMPRESSION)
    compress_ratio = (float(len(compzFile)) - float(len(deflateData))) / float(len(compzFile))  
    print('Compressed: %d%%' % (100.0 * compress_ratio))

    compressedOutFile = open('%s-comp' % fileName, 'wb')
    compressedOutFile.write(deflateData)
    compressedOutFile.close()

def inflateFiles(fileName):
    compressedInFile = open('%s-comp' % fileName, 'rb').read()
    inflateData = zlib.decompress(compressedInFile)

    inflatedFile = open('%s-df' % fileName, 'wb')
    print('Inflated data is being written to: %s-df' % fileName)
    inflatedFile.write(inflateData)

def main():
    cmd = input('TODO: ')

    if cmd == 'compress':
        dFile = input('choose a file to compress: ')
        deflateFiles(dFile)
    elif cmd == 'decompress':
        iFile = ('Choose a file to inflate: ')
        inflateFiles(iFile)
    else:
        print('Invalid command. Please choose to compress a file or decompress a file.')


if __name__ == "__main__":
    main()
