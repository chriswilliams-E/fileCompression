#!/usr/bin/python3

import zlib

def deflateFiles(d_fileName):
    compzFile = open(d_fileName, 'rb').read()
    print('Deflating %s' % d_fileName)
    deflateData = zlib.compress(compzFile, zlib.Z_BEST_COMPRESSION)
    compress_ratio = (float(len(compzFile)) - float(len(deflateData))) / float(len(compzFile))  
    print('Compressed: %d%%' % (100.0 * compress_ratio))

    compressedOutFile = open('%s-comp' % d_fileName, 'wb')
    compressedOutFile.write(deflateData)
    compressedOutFile.close()

def inflateFiles(i_fileName):
    compressedInFile = open('%s' % i_fileName, 'rb').read()
    inflateData = zlib.decompress(compressedInFile)

    inflatedFile = open('%s-df' % i_fileName, 'wb')
    print('Inflated data is being written to: %s-df' % i_fileName)
    inflatedFile.write(inflateData)

def main():
    cmd = input('TODO: ')

    if cmd == 'compress':
        dFile = input('choose a file to compress: ')
        deflateFiles(dFile)
    elif cmd == 'decompress':
        iFile = input('Choose a file to inflate: ')
        inflateFiles(iFile)
    else:
        print('Invalid command. Please choose to compress a file or decompress a file.')


if __name__ == "__main__":
    main()
