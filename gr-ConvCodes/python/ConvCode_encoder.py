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

class ConvCode_encoder(gr.interp_block):
    """
    docstring for block ConvCode_encoder
    """
    def __init__(self):
        gr.interp_block.__init__(self,
            name="ConvCode_encoder",
            in_sig=[numpy.byte],
            out_sig=[numpy.byte], interp = 2)
        self.state_machine = {'00':[['00','00'],['11','10']],'01':[['11','00'],['00','10']],'10':[['01','01'],['10','11']],'11':[['10','01'],['01','11']]}
        self.resolve = {'00':[False,False],'01':[False,True],'10':[True,False],'11':[True,True]}
        self.current_state = '00'

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # inp = numpy.array(in0)
        # oup = numpy.array(out)
        # print(inp.shape)
        # print(oup.shape)
        # print(in0)
        # <+signal processing here+>
        for i in range(0, len(in0)):
            sample = in0[i]
            result = self.state_machine[self.current_state][sample]
            self.current_state = result[1]
            # print(result)
            out[2*i] = self.resolve[result[0]][0]
            out[2*i+1] = self.resolve[result[0]][1]
        # out[:] = in0
        return len(output_items[0])

