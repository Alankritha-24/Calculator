import numpy as np
import soundfile as sf

#new_data = np.empty([25000,]) #creating an empty array for new file to be generated from original file

loc="back"

ind = 1
for j in range(0,81):
	b= "new/"+loc+"/"+loc+str(j)+".wav"
	data, samplerate = sf.read(b) #reading audio file using soundfile library
	print(len(data), samplerate)
	x= len(data)
	p = 25000-x
	d = int(p/25)
	new_data = np.zeros([25000,])
	y = (25000//2)-(p//2)
	for y in range(0 ,25):#p, d):   
		for i in range(0,x):
			new_data[y+i] =data[i]
		a = "newout/"+loc+"/"+loc+str(ind)+".wav"    #total length becomes 25000
		ind += 1
		sf.write(a, new_data, samplerate)  #audio files are written back to harddisk
		print(len(new_data))
