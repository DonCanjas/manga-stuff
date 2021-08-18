import vapoursynth as vs
import os, glob
core = vs.get_core()

imgs = list()
lst = glob.glob("input_folder*.jpg") #change jpg to whatever extension the desired input files are

for srcfile in lst:
  img = core.imwri.Read(srcfile)
  img = core.resize.Spline36(img, format=vs.RGBS)
  img = core.ccd.CCD(img, 20)
  imgs.append(img)
  
core.imwri.Write(core.std.Splice(imgs), "PNG", "output_folder/denoised_%03d.png").set_output()
