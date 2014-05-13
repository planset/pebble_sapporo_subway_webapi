#!/bin/bash

mkdir __mecab_build
pushd __mecab_build

#
# mecab
#
# mac: brew install mecab
# ubuntu: build

#
# mecab-ipadic
#
# mac: brew install mecab-ipadic
#
# ubuntu: build

#
# mecab-python
#
# mac,ubuntu: build
tar zxf ../mecab/mecab-python-0.996.tar.gz
pushd mecab-python-0.996
python setup.py build
python setup.py install
popd

popd
rm -Rf __mecab_build

