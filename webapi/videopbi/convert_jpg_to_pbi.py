from __future__ import print_function
import os

import bitmapgen

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
DEFAULT_CONFIG = os.path.join(CUR_DIR, 'config.json')

CMD2 = 'convert -size 144x168 {input_filepath} -resize 144x168 -monochrome {output_filepath}'

SKIP_MS = 250


class Args(object):
    pass

def execute(cmd):
    return os.system(cmd)

def convert(srcfilepath):
    pngfilepath = srcfilepath.replace('.jpg', '.png')
    pbifilepath = srcfilepath.replace('org_', '').replace('.jpg', '.pbi')

    r = execute(CMD2.format(input_filepath=srcfilepath,
        output_filepath=pngfilepath))
    if r != 0:
        break

    bitmapgen_args = Args()
    bitmapgen_args.input_png = pngfilepath
    bitmapgen_args.output_pbi = pbifilepath
    bitmapgen.cmd_pbi(bitmapgen_args)

    os.remove(pngfilepath)



