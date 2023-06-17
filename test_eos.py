#!/usr/bin/env python

from  __future__ import print_function
import time

import ROOT

import click

LFN = "/store/user/schoef/TTbb_MS_EFT/22-05-12/230610_144822/0000/TOP-RunIISummer20UL18HLT-00004_862.root"

@click.command()
@click.option('--redirector', default="eos.grid.vbc.ac.at")
def main(redirector):
    
    start = time.time()
    file = ROOT.TFile.Open("root://{}/{}".format(redirector, LFN), "READ")
    tree = file.Get("Events")
    nr_events = tree.GetEntries()
    for i, event in enumerate(tree):
        if i % 100 == 0:
            print("Events: {:>4}/{:>4}".format(i,nr_events))
    total = time.time() - start
    
    print("Events/second: {:4.2f}".format(nr_events/total))              

if __name__ == '__main__':
    main()