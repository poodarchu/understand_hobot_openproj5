# -*- coding: utf-8 -*-

from structures import actions, positions, classes
from snap_label_to_grid import snap2grid
from snap_label_to_grid import Modes

from pyltp import Segmentor

segmentor = Segmentor()
segmentor.load("/Users/poodarchu/Libs/ltp_data_v3.4.0/cws.model")

with open('labels.txt') as labels:
    objects = {}
    for label in labels.readlines():
        cls, lt_x, lt_y, rb_x, rb_y = label.split(" ")
        if cls not in objects.keys():
            objects[cls] = []
            objects[cls].append(map(int, [lt_x, lt_y, rb_x, rb_y]))
        else:
            objects[cls].append(map(int, [lt_x, lt_y, rb_x, rb_y]))


with open('./commands.txt', 'r') as fin:
    commands = fin.readlines()
    for command in commands:
        words = segmentor.segment(command)
        print " ".join(words)

        action = []
        position = []
        cls = []

        for word in words:
            if word in actions.keys():
                action.append(actions[word])
            if word in positions.keys():
                position.append(positions[word])
            if word in classes.keys():
                cls.append(classes[word])

            print action, position, cls

            try:
                cls_objects = objects[cls[0]]
                length = len(cls_objects)
            except:
                continue
            try:
                cls_objects = snap2grid(cls_objects, mode=position[0][0])
                if position[0][2] < length:
                    print cls_objects[position[0][2]], "YYYYYYYYYYY"
                else:
                    print cls_objects[length-1]

                continue
            except:
                print "NNNNNNNNN"

segmentor.release()
