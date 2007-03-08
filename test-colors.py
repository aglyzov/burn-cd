#!/usr/bin/python -O
# -*- coding: cp1251 -*-

COLOR_0		= "\033[m"	# �����
COLOR_1		= "\033[1m"	# ������ (bold)
COLOR_2		= "\033[0;32m"	# ������
COLOR_3		= "\033[1;32m"	# ����-������
COLOR_4		= "\033[0;33m"	# �����
COLOR_5		= "\033[1;33m"	# ����-�����
COLOR_6		= "\033[0;36m"	# ���������
COLOR_7		= "\033[1;36m"	# ����-���������
COLOR_8		= "\033[1;31m"	# ����-�������
COLOR_9		= "\033[1;34m"	# ����-�����

if __name__ == '__main__':
	print
	print '1: %s[%s=====================%s*        %s] %s10.3x (1.5 MB/s)%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, COLOR_2, COLOR_0)
	print '2: %s[%s=====================%s*        %s] %s10.3x %s(%s1.5 MB/s%s)%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_5, COLOR_9, COLOR_5, COLOR_9, COLOR_0)
	print '3: %s[%s=====================%s*        %s] %s10.3x %s(%s1.5 MB/s%s)%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_2, COLOR_9, COLOR_2, COLOR_9, COLOR_0)
	print '4: %s[%s=====================%s*        %s] %s10.3x %s(%s1.5 MB/s%s)%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_3, COLOR_9, COLOR_3, COLOR_9, COLOR_0)
	print '5: %s[%s=====================%s*        %s] %s10.3x %s(%s1.5 MB/s%s)%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_3, COLOR_9, COLOR_5, COLOR_9, COLOR_0)
	print '6: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_3, COLOR_2, COLOR_3, COLOR_2, COLOR_0)
	print '7: %s[%s=====================%s*        %s] %s10.3%s%sx %s1.5%s%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_5, COLOR_0, COLOR_1, COLOR_5, COLOR_0, COLOR_1, COLOR_0)
	print '8: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_5, COLOR_4, COLOR_5, COLOR_4, COLOR_0)
	print '9: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_7, COLOR_6, COLOR_7, COLOR_6, COLOR_0)
	print 'A: %s[%s=====================%s*        %s] %s10.3%s%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_8, COLOR_0, COLOR_1, COLOR_7, COLOR_9, COLOR_0)
	print 'B: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_7, COLOR_9, COLOR_7, COLOR_9, COLOR_0)
	print 'C: %s[%s=====================%s*        %s] %s10.3%s%sx %s1.5%s%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_3, COLOR_0, COLOR_1, COLOR_3, COLOR_0, COLOR_1, COLOR_0)
	print 'D: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_3, COLOR_0, COLOR_3, COLOR_0, COLOR_0)
	print 'E: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_2, COLOR_0, COLOR_2, COLOR_0, COLOR_0)
	print 'F: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_3, COLOR_6, COLOR_3, COLOR_6, COLOR_0)
	print 'G: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_5, COLOR_6, COLOR_5, COLOR_6, COLOR_0)
	print 'H: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_5, COLOR_0, COLOR_5, COLOR_0, COLOR_0)
	print 'I: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_0+COLOR_1, COLOR_9, COLOR_0+COLOR_1, COLOR_9, COLOR_0)
	print 'J: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_0+COLOR_1, COLOR_6, COLOR_0+COLOR_1, COLOR_6, COLOR_0)
	print 'K: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_0+COLOR_1, COLOR_2, COLOR_0+COLOR_1, COLOR_2, COLOR_0)
	print 'L: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_5, COLOR_4, COLOR_7, COLOR_6, COLOR_0)
	print 'M: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_7, COLOR_6, COLOR_3, COLOR_2, COLOR_0)
	print 'N: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_3, COLOR_2, COLOR_5, COLOR_4, COLOR_0)
	print 'O: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_0+COLOR_1, COLOR_6, COLOR_5, COLOR_6, COLOR_0)
	print 'P: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_5, COLOR_6, COLOR_3, COLOR_6, COLOR_0)
	print 'Q: %s[%s=====================%s*        %s] %s10.3%sx %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_5, COLOR_6, COLOR_0+COLOR_1, COLOR_6, COLOR_0)
	print 'R: %s[%s=====================%s*        %s][%s10.3%sx  %s1.5%sMB/s%s]%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_0+COLOR_1, COLOR_6, COLOR_0+COLOR_1, COLOR_6, COLOR_9, COLOR_0)
	print 'S: %s[%s=====================%s*        %s] %s10.3%sx %s( %s1.5%sMB/s%s)%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_0+COLOR_1, COLOR_6, COLOR_9, COLOR_0+COLOR_1, COLOR_6, COLOR_9, COLOR_0)
	print 'T: %s[%s=====================%s*        %s] %s10.3%sx  %s1.5%sMB/s%s\n' % \
		(COLOR_9, COLOR_5, COLOR_8, COLOR_9, \
		COLOR_0+COLOR_1, COLOR_6, COLOR_0+COLOR_1, COLOR_6, COLOR_0)
	
	# 10.3x  1.5MB/s
	# that was fast!
	# *FAST*  *FAST*
	# **************
	# >>>>>>>>>>>>>>
	# ??.?x ??.?MB/s
	# ....x ....MB/s
	#  *** FAST *** 
	# FAST FAST FAST
	#    * FAST *
	#     *FAST*
	# ..............
	# --.-x --.-MB/s
	# __._x __._MB/s
	# pre-formatting
