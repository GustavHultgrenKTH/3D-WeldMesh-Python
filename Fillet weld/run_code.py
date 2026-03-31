import os, filletweld3d

base = r"C:\Users\gusta\OneDrive - KTH\00_GitHub\3D-ButtWeldMesh-Python\Fillet weld"
param_file = os.path.join(base, "V5_5_2_cs_cs.txt")
weld_file  = os.path.join(base, "V5_5_2_cs_cs.pcd")  # or .mat

bw = filletweld3d.initialize()
try:
    inputFile = bw.weld_3D(param_file, weld_file, "V5_5_2_cs_cs", nargout=1)
    print("inputFile:", inputFile)
    #print("nodeFile:", nodeFile)
    #print("elemFile:", elemFile)
finally:
    try: bw.terminate()
    except Exception: pass
