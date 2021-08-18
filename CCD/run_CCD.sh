#!/bin/bash
for file in *.py
do
vspipe $file .
done
