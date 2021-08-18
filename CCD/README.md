CCD - Camcorder Color Denoise
-----------------------------
This vapoursynth script applies chroma denoise to every .jpg file in a specific folder.   
Just change the input and output folders to the desired, as well the input and output file formats.  

Thanks to Devek1 for helping me creating the script.

Dependencies
-----------------------------
- [vapoursynth](https://github.com/vapoursynth/vapoursynth)  
- [CCD](https://github.com/End-of-Eternity/vs-ccd)  

Usage
-----------------------------

After modifying the script to input, output and denoising strength to your preferences, run the shell script `run_CCD.sh`.  
The script should be in the same folder as `CCD.py`.

Sample
-----------------------------
Done using the default settings. (I'd personally use a higher strength on this one, like 30)  
  
Raw -----> Filtered   
![](https://github.com/DonCanjas/manga-stuff/blob/main/CCD/samples/raw.png) 
![](https://github.com/DonCanjas/manga-stuff/blob/main/CCD/samples/denoised_CCD.png)
