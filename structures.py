# -*- coding: utf-8 -*-

from snap_label_to_grid import Modes

positions = {
    "左边" : (Modes.LeftRight, 'left', 0),
    "右边" : (Modes.LeftRight, 'right', -1),
    "上边" : (Modes.TopDown, 'top', 0),
    "下边" : (Modes.TopDown, 'down', -1),
    "中间" : (Modes.LeftMiddleRight, 'middle', 1),
    "左上角" : (Modes.LTRB, 'lt', 0),
    "左下角" : (Modes.LTRB, 'lb', 1),
    "右上角" : (Modes.LTRB, 'rt', 2),
    "右下角" : (Modes.LTRB, 'rb', 3)
}

classes = {
    "人" : 'person',
    "衣服" : 'cloth',
    "水瓶" : 'bottle',
    "椅子" : 'chair',
    "电脑" : 'laptop',
    "手机" : 'phone',
    "鞋"   : 'shoes',
    "手表" : 'watch',
    "车" : 'car'
}

actions = {
    "谁" : 'popupwindow',
    "什么" : 'sidewindow'
}