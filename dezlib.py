#!/usr/bin/python3

import zlib

fileName = input('Enter name of zlib file: ' )

def deflater(fileToDeflate):
    compzFile = open(fileToDeflate, 'rb').read()
    print('Deflating %s' % fileToDeflate)
    deflateData = zlib.compress(compzFile, zlib.Z_BEST_COMPRESSION)
    #print(len(compzFile))
    compress_ratio = (float(len(compzFile)) - float(len(deflateData))) / float(len(compzFile))  
    print('Compressed: %d%%' % (100.0 * compress_ratio))

    compressedOutFile = open(fileName + '.dat', 'w')
    compressedOutFile.write(str(deflateData))
    compressedOutFile.close()

deflater(fileName)

'''
zFile = open(fileName, 'rb')
print('Inflating %s' % fileName)
inflateData = zlib.decompress(zFile.read())
zFile.close()

inflatedFile = open('%s-df' % fileName, 'w')
print('Inflated data is being written to: %s' % inflatedFile)
inflatedFile.write(inflateData)
inflatedData.close()
'''

    
