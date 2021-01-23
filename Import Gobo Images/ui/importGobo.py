import os
import vs


# #Gobo size
# GoboSize = 24

# #Gobo Scale
# GoboScale = 1.05

#Convert size to a bounding box centered on 0,0

def ConvertSize(GoboSize):
	bound = GoboSize/2
	BBL = (-bound,bound)
	BBR = (bound,-bound)

	return BBL, BBR





def ImportSym(GoboSize, GoboScale):

	symCreatedCnt = 0

	# define a location to import the images
	importPt = (0,0)

	#Set Origin
	xOrigin = 0
	yOrigin = 0

	#Set Final Bounding Box Size
	BBL, BBR = ConvertSize(GoboSize)

	major, minor, maintenance, platform = vs.GetVersion()
	isMac = False
	if platform == 1: isMac = True

	err, dirPath = vs.GetFolder( 'Select a Folder' )
	if err == 0: # no-error
		hsfDirPath = dirPath
		if isMac: ok, hsfDirPath = vs.ConvertPosix2HSFPath( dirPath )

		fileIndex = 1
		while True: # loop the files
			fileName = vs.GetFilesInFolder( hsfDirPath, fileIndex )
			fileIndex += 1

			if fileName == '': # no more files
				return symCreatedCnt

			name, ext = os.path.splitext( fileName )
			if ext.lower() == '.png' or ext.lower() == '.jpg' or ext.lower() == '.jpeg' or ext.lower() == '.gif':
				imagePath = os.path.join( dirPath, fileName )

				vs.BeginSym( name )
				hImage = vs.ImportImageFile( imagePath, importPt )

				#Set image size
				hImage = vs.PickObject(0,0)
				vs.SetBBox(hImage, BBL, BBR)

				#Draw Oval and set HANDLE var
				OvalBBL = (xOrigin,yOrigin)
				OvalBBR = ((abs(BBL[0])+abs(BBR[0])),-(abs(BBL[1])+abs(BBR[1])))
				vs.Oval(OvalBBL, OvalBBR)
				hCrop = vs.LNewObj()

				#Scale image
				vs.HScale2D(hImage, 0, 0, GoboScale, GoboScale, 0)

				#Move the crop oval to the bottom right corner of the gobo image
				xCropMove = ((BBR[0]*GoboScale)-BBR[0])
				yCropMove = ((BBR[1]*GoboScale)-BBR[1])
				vs.HMove(hCrop, xCropMove, yCropMove)

				#Crop dat
				vs.SetImageCropObject(hImage, hCrop)

				#Finish
				vs.EndSym()
				symCreatedCnt += 1



# symCreated = ImportSym(GoboSize, GoboScale)

# vs.AlrtDialog( 'Done! Created ', symCreated , ' symbols.')
