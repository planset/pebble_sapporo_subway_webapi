#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MeCab

KATA = u'ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ'
HIRA = u'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんばここ'


def kata2hira(text):
    """
    :param text: text は utf-8 または unicode で渡すこと
    :return: カタカナをひらがなに変換した unicode 文字列
    """
    def _kata2hira(c): 
        i = KATA.find(c)
        return HIRA[i] if i>0 else c
    text = text.decode('utf-8') if not isinstance(text, unicode) else text
    return ''.join([ _kata2hira(c) for c in text])

def text2kata(text):
    """
    :param text: text は utf-8 または unicode で渡すこと
    :return: 文字列をカタカナに変換した unicode 文字列
    """
    m = MeCab.Tagger("-Ochasen")
    text = text.encode('utf-8') if isinstance(text, unicode) else text
    def _get_kana(items): return items[1] if len(items) > 1 else ''
    return ''.join([_get_kana(line.split("\t")) for line in m.parse(text).split("\n")]).decode('utf-8')

def text2hira(text):
    """
    :param text: text は utf-8 または unicode で渡すこと
    :return: 文字列をひらがなに変換した unicode 文字列

    >>> print text2hira("今日は天気が良い")
    "きょうはてんきがよい"
    """
    return kata2hira(text2kata(text))


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        sys.exit(-1)
    print text2hira(sys.argv[1])


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
