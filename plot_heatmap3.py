import matplotlib.pyplot as plt
import numpy as np

strad = '_AVERAGE_4000'
#strad = ''

rows = 3
cols = 3

ytix_loc = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
xtix_loc = [0.5, 2.5, 4.5, 6.5, 8.5]
ytix = [0.0001,0.0002, 0.0003, 0.0004, 0.0005, 0.001, 0.002, 0.003, 0.004, 0.005]
xtix = [0,20,40,60,80, 100]

YY = np.log10(np.asarray([0.00005, 0.00015, 0.00025, 0.00035, 0.00045, 0.00055, 0.0015, 0.0025, 0.0035, 0.0045, 0.0055]))
XX = np.asarray( [0,10,20,30,40,50,60,70,80,90,100])

#rect = 0.1,0.1,0.9,0.8
#fig = plt.figure()
#ax = fig.add_axes(rect)
#cov = np.genfromtxt("cov_map.csv", delimiter=',')

e_min = 0
e_max = 30
a_min = 0
a_max = 55000
c_min = 0
c_max = 0.08

fs = 16 # font size
fsa = 18 # font size for annotation

#cov = cov[4:,:]
subd =  'mut_0_hl_type_1/'

def plot_map(AX, fname, mmin=0,mmax=1, annot='A', xoff=False,yoff=False, xlab='None', ylab='None', aspect=False, row_lab=None, col_lab=None, log=False):

	global xtix, ytix, xtix_loc, ytix_loc, fsa, fs

	mmap = np.genfromtxt(fname, delimiter=',')
	if log:
		mmap = np.log(mmap)
	im = AX.pcolor(mmap, vmin=mmin, vmax=mmax)
	plt.colorbar(im, ax=AX)
	AX.annotate(annot, (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')
	if row_lab != None:
		AX.annotate(row_lab, xy=(0.0, 0.5), size='x-large', ha='right', va='center', xytext= (-4.5, 5))#(-ax.yaxis.labelpad - pad, 0),xycoords=ax.yaxis.label, textcoords='offset points'
	if col_lab != None:
		AX.set_title(col_lab)

	AX.set_xticks(xtix_loc)
	AX.set_yticks(ytix_loc)
	if xoff:
		AX.set_xticklabels('')
	else:
		AX.set_xticklabels(xtix)
	if yoff:
		AX.set_yticklabels('')
	else:
		AX.set_yticklabels(ytix)

	if xlab != 'None':
		AX.set_xlabel(xlab, fontsize = fs)
	if ylab != 'None':
		AX.set_ylabel(ylab, fontsize = fs)

	if aspect:
		AX.set_aspect('equal', 'datalim')


#fig, axes = plt.subplots(3,3, figsize=(18,18))  
fig, axes = plt.subplots(3,3, figsize=(22,18))  
AX = axes.flatten()

plot_map(AX[0], 'is3_map_mai_0'+strad+'.csv', mmax=0.005, xoff=True, row_lab = 'MAI = 0.0', col_lab='mean IS3', ylab='immigration', annot='A')
plot_map(AX[1], 'is1_map_mai_0'+strad+'.csv', mmax=300000, xoff=True,yoff=True, col_lab='total IS1', annot='B')   
plot_map(AX[2], 'mean_cv_map_mai_0'+strad+'.csv', mmax=1, xoff=True, yoff=True, col_lab='mean CV', annot='C') #, log=True) 

plot_map(AX[3], 'is3_map_mai_0.5'+strad+'.csv', mmax=0.005, xoff=True, row_lab = 'MAI = 0.5', ylab='immigration', annot='D')
plot_map(AX[4], 'is1_map_mai_0.5'+strad+'.csv', mmax=300000, xoff=True,yoff=True, annot='E')
plot_map(AX[5], 'mean_cv_map_mai_0.5'+strad+'.csv', mmax=1, xoff=True, yoff=True, annot='F') #,log=True) 

plot_map(AX[6], 'is3_map_mai_1.0'+strad+'.csv', mmax=0.005, xlab='habitat loss', ylab='immigration', annot='G', row_lab='MAI = 1.0')
plot_map(AX[7], 'is1_map_mai_1.0'+strad+'.csv', mmax=300000, xlab='habitat loss', yoff=True, annot='H')
plot_map(AX[8], 'mean_cv_map_mai_1.0'+strad+'.csv', mmax=1, xlab='habitat loss', yoff=True, annot='I') #, log=True)

#plot_map(AX[0], 'test.csv', mmax=54000, xoff=True, row_lab = 'MAI = 0.0', col_lab='Extinctions', ylab='immigration')
#lot_map(AX[3], 'test2.csv', mmax=60, xoff=True, yoff=True)
#plot_map(AX[8], 'test.csv', mmax=54000, xoff=True,yoff=True, xlab='habitat loss')

#plt.subplots_adjust(wspace=0.3, left=0.3)
plt.subplots_adjust(wspace=0.3, left=0.16)
plt.savefig("heatmap3"+strad+".png")
plt.show()


if False:
	###################################################################################################
	## EXTINCTIONS		
	aa = plt.subplot(rows, cols,1)
	ext = np.genfromtxt(subd + "extinction_map.csv", delimiter=',')
	#im = plt.pcolor(ext)
	im = plt.pcolor(ext, vmin=e_min, vmax=e_max)
	#im = plt.pcolor(XX,YY,ext)

	plt.ylabel("immigration", size=fs)
	#ax.set_yticklabels([0.0001,0.0005,0.001, 0.002,0.003,0.004,0.005])
	aa.set_xticks(xtix_loc)
	aa.set_yticks(ytix_loc)
	aa.set_yticklabels(ytix)
	aa.set_xticklabels(xtix)
	aa.annotate("MAI = 0.0", xy=(0.0, 0.5), size='x-large', ha='right', va='center', xytext= (-3, 5))#(-ax.yaxis.labelpad - pad, 0),xycoords=ax.yaxis.label, textcoords='offset points'
	aa.annotate("A", (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')
	plt.title('Mean number of extinctions')
	plt.colorbar(im)

	###################################################################################################
	## TOTAL ABUNDANCE
	aa = plt.subplot(rows, cols,2)
	ext = np.genfromtxt(subd + "tot_abundance_map.csv", delimiter=',')
	im = plt.pcolor(ext, vmin=a_min, vmax=a_max)

	aa.set_xticks(xtix_loc)
	aa.set_yticks(ytix_loc)
	aa.set_xticklabels(xtix)
	aa.set_yticklabels(ytix)
	aa.annotate("B", (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')

	plt.title('Mean number of individuals')
	plt.colorbar(im)
	###################################################################################################
	## COV
	aa = plt.subplot(rows, cols,3)
	cov = np.genfromtxt(subd + "cov_map.csv", delimiter=',')
	im = plt.pcolor(cov, vmin=c_min, vmax=c_max)

	aa.set_xticks(xtix_loc)
	aa.set_yticks(ytix_loc)
	aa.set_xticklabels(xtix)
	aa.set_yticklabels(ytix)
	aa.annotate("C", (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')

	plt.title('Mean CoV: temporal variability')
	plt.colorbar(im)


	subd =  'mut_0.5_hl_type_1/'
	###################################################################################################
	## EXTINCTIONS		
	aa = plt.subplot(rows, cols,4)
	ext = np.genfromtxt(subd + "extinction_map.csv", delimiter=',')
	im = plt.pcolor(ext, vmin=e_min, vmax=e_max)
	#im = plt.pcolor(XX,YY,ext)

	plt.ylabel("immigration", size=fs)
	#ax.set_yticklabels([0.0001,0.0005,0.001, 0.002,0.003,0.004,0.005])
	aa.set_xticks(xtix_loc)
	aa.set_yticks(ytix_loc)
	aa.set_yticklabels(ytix)
	aa.set_xticklabels(xtix)
	aa.annotate("MAI = 0.5", xy=(0.0, 0.5), size='x-large', ha='right', va='center', xytext= (-3, 5))#(-ax.yaxis.labelpad - pad, 0),xycoords=ax.yaxis.label, textcoords='offset points'
	aa.annotate("D", (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')
	plt.colorbar(im)

	###################################################################################################
	## TOTAL ABUNDANCE
	aa = plt.subplot(rows, cols,5)
	ext = np.genfromtxt(subd + "tot_abundance_map.csv", delimiter=',')
	im = plt.pcolor(ext, vmin=a_min, vmax=a_max)

	#ax.set_xlabel("percentage habitat destroyed")
	#ax.set_ylabel("immigration")
	#ax.set_yticklabels([0.0001, 0.0005, 0.001, 0.002,0.003,0.004,0.005])
	aa.set_xticks(xtix_loc)
	aa.set_yticks(ytix_loc)
	aa.set_yticklabels(ytix)
	aa.set_xticklabels(xtix)

	aa.annotate("E", (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')
	plt.colorbar(im)
	###################################################################################################
	## COV
	aa = plt.subplot(rows, cols,6)
	cov = np.genfromtxt(subd + "cov_map.csv", delimiter=',')
	im = plt.pcolor(cov, vmin=c_min, vmax=c_max)

	aa.set_xticks(xtix_loc)
	aa.set_yticks(ytix_loc)
	aa.set_xticklabels(xtix)
	aa.set_yticklabels(ytix)

	aa.annotate("F", (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')
	plt.colorbar(im)


	subd =  'mut_1.0_hl_type_1/'
	###################################################################################################
	## EXTINCTIONS		
	aa = plt.subplot(rows, cols,7)
	ext = np.genfromtxt(subd + "extinction_map.csv", delimiter=',')
	im = plt.pcolor(ext, vmin=e_min, vmax=e_max)
	#im = plt.pcolor(XX,YY,ext)

	plt.ylabel("immigration", size=fs)
	plt.xlabel("% habitat destruction", size=fs)
	aa.set_xticks(xtix_loc)
	aa.set_yticks(ytix_loc)
	aa.set_yticklabels(ytix)
	aa.set_xticklabels(xtix)
	aa.annotate("G", (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')

	pad = 0 # in points
	aa.annotate("MAI = 1.0", xy=(0.0, 0.5), size='x-large', ha='right', va='center', xytext= (-3, 5))#(-ax.yaxis.labelpad - pad, 0),xycoords=ax.yaxis.label, textcoords='offset points'

	plt.colorbar(im)

	###################################################################################################
	## TOTAL ABUNDANCE
	aa = plt.subplot(rows, cols,8)
	ext = np.genfromtxt(subd + "tot_abundance_map.csv", delimiter=',')
	im = plt.pcolor(ext, vmin=a_min, vmax=a_max)

	plt.xlabel("% habitat destruction", size=fs)
	#ax.set_yticklabels([0.0001, 0.0005, 0.001, 0.002,0.003,0.004,0.005])
	aa.set_xticks(xtix_loc)
	aa.set_yticks(ytix_loc)
	aa.set_yticklabels(ytix)
	aa.set_xticklabels(xtix)
	aa.annotate("H", (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')

	plt.colorbar(im)
	###################################################################################################
	## COV
	aa = plt.subplot(rows, cols,9)
	cov = np.genfromtxt(subd + "cov_map.csv", delimiter=',')
	im = plt.pcolor(cov, vmin=c_min, vmax=c_max)

	plt.xlabel("% habitat destruction", size=fs)
	#ax.set_yticklabels([0.0001,0.0005,0.001, 0.002,0.003,0.004,0.005])
	aa.set_xticks(xtix_loc)
	aa.set_yticks(ytix_loc)
	aa.set_xticklabels(xtix)
	aa.set_yticklabels(ytix)
	aa.annotate("I", (0,0), (0.02,0.9), color='white', fontsize= fsa, fontweight='bold', xycoords='data', textcoords='axes fraction')

	plt.colorbar(im)

	#plt.tight_layout()
	plt.subplots_adjust(wspace=0.3)
	#plt.tight_layout()
	#plt.savefig("heatmap1"+strad+".png")
	plt.show()

