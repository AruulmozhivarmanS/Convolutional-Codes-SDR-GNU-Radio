#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 Aruul Mozhi Varman S.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class ConvCode_decoder(gr.decim_block):
    """
    docstring for block ConvCode_decoder
    """
    def __init__(self):
        gr.decim_block.__init__(self,
            name="ConvCode_decoder",
            in_sig=[numpy.byte],
            out_sig=[numpy.byte], decim = 2)
        # self.state_machine = {'00':['00','11'],'01':['11','00'],'10':['01','10'],'11':['10','01']}
        # self.state_machine_result = {'00':['00','10'],'01':['00','10'],'10':['01','11'],'11':['01','11']}
        self.state_machine = {'00':[['00','00'],['11','10']],'01':[['11','00'],['00','10']],'10':[['01','01'],['10','11']],'11':[['10','01'],['01','11']]}
        self.distance = {'00' : 0, '01' : 0, '10' : 0, '11' : 0}
        self.resolve = {'00':[0,0],'01':[0,1],'10':[1,0],'11':[1,1]}
        self.current_state = '00'


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        for i in range(0, len(in0)/2):
            in1 = in0[2 * i]
            in2 = in0[2 * i + 1]
            calculate = self.state_machine[self.current_state]
            # result = self.resolve[cal]
            a1 = self.resolve[calculate[0][0]]
            a2 = self.resolve[calculate[1][0]]
            # print(a1)
            # print(a2)
            # result = (a1[0] ^ in1 + a1[1] * in2) < (a2[0] ^ in1 + a2[1] * in2) ? 0:1
            # d1 = (a1[0] ^ in1) + (a1[1] ^ in2)
            # d2 = (a2[0] ^ in1) + (a2[1] ^ in2)
            self.distance[calculate[0][1]] += (a1[0] ^ in1) + (a1[1] ^ in2)
            self.distance[calculate[1][1]] += (a2[0] ^ in1) + (a2[1] ^ in2)
            result, self.current_state =  (0, calculate[0][1]) if (self.distance[calculate[0][1]] < self.distance[calculate[1][1]]) else (1, calculate[1][1])
            # self.current_state = calculate[0][1] if ((a1[0] ^ in1) + (a1[1] ^ in2)) < ((a2[0] ^ in1) + (a2[1] ^ in2)) else calculate[1][1]
            # self.current_state = state
            # print(self.current_state)
            # print(result)
            # print(self.distance)
            out[i] = result
        return len(output_items[0])

