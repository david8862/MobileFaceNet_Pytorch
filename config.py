#!/usr/bin/env python3
# -*- coding: utf-8 -*-
BATCH_SIZE = 128
SAVE_FREQ = 1
TEST_FREQ = 1
TOTAL_EPOCH = 70

RESUME = ''
SAVE_DIR = './model'
MODEL_PRE = 'CASIA_B512_'


#CASIA_DATA_DIR = '/home/xiaocc/Documents/caffe_project/sphereface/train/data'
#LFW_DATA_DIR = '/home/xiaocc/Documents/caffe_project/sphereface/test/data'
CASIA_DATA_DIR = '/mnt/disk02/dataset/face_recognition/CASIA-align-112-96'
LFW_DATA_DIR = '/mnt/disk02/dataset/face_recognition/lfw-align-112-96'

#GPU = 0, 1
GPU = 0

