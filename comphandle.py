#!/usr/bin/python3

import zlib
import os

fileName = input('Enter name of file: ')

compzFile = open(fileName, 'rb').read()
print('Deflating %s' % fileName)
deflateData = zlib.compress(compzFile, zlib.Z_BEST_COMPRESSION)
compress_ratio = (float(len(compzFile)) - float(len(deflateData))) / float(len(compzFile))  
print('Compressed: %d%%' % (100.0 * compress_ratio))

compressedOutFile = open('%s-comp' % fileName, 'wb')
compressedOutFile.write(deflateData)
compressedOutFile.close()

compressedInFile = open('%s-comp' % fileName, 'rb').read()
inflateData = zlib.decompress(compressedInFile)

inflatedFile = open('%s-df' % fileName, 'wb')
print('Inflated data is being written to: %s-df' % fileName)
inflatedFile.write(inflateData)
