# EUFS Darknet

[AlexeyAB's darknet](https://github.com/AlexeyAB/darknet) adapted for the Edinbrugh Univeristy's Formula Student team.

TODO: small description of this repo and some of its output videos and images 

### How to install it

1. (Optional) Install OpenCV with ffmpeg support using [these instructions](https://github.com/NotAnyMike/darknet_EUFS#Installing-OpenCV-with-ffmpeg-Support).
	
	NOTE: This step is required if you'd like to pass videos/camera input into the program for object detection; it is highly recommended
2. Clone this repo
3. In the `darknet_EUFS` folder, modify `MakeFile` based on [these instructions](https://github.com/AlexeyAB/darknet#how-to-compile-on-linux)
4. Compile it using `make`
5. Download stable weights from here and add the downloaded `weights` directory to the `EUFS` directory

## How to run it

* For Single Images: 

	1. cd into EUFS: `cd EUFS`
	2. run the command: `./darknet detector test cfg/cones-obj.data cfg/cones-obj.cfg <path to weights file> -i 0 -thresh 0.05 <path to image>`

	For example: `./darknet detector test cfg/cones-obj.data cfg/cones-obj.cfg weights/v1/yolo-cones_2000.weights -i 0 -thresh 0.05 cones/frame0030.jpg`

	The command saves the images with predictions in the `EUFS` directory as `predictions.jpg`

* For Video:

	1. cd into EUFS: `cd EUFS`
	2. run the command: `./darknet detector demo cfg/cones-obj.data cfg/cones-obj.cfg <path to weight file> -dont_show -thresh 0.05 <path to video file>`

	For example: `./darknet detector demo cfg/cones-obj.data cfg/cones-obj.cfg weights/v1/yolo-cones_2000.weights -dont_show -thresh 0.05 videos/out.mp4`

* For Several Images:
	
	1. cd into EUFS: `cd EUFS`
	2. run the command: `batch.py <path to directory with images> <type of image (default: jpg)>`

	For example: `batch.py cones`

	This will create a directory called `pred_cones` with images containing the boudning box and label of the prediction(s)

**Flags:** 
* `tresh x`: outputs predictions that have confidence greater than `x*100`%
* `dont_show`: doesn't open the image/video after making predictions 

## How to Retrain It

TODO

## Extra Information

### Weights

| name | description |
| --- | --- |
| `darknet19_448.conv.23` | original from yolo used in retraining |
| `v1/...2000.weights` | **Stable weights** for cones |

### Installing OpenCV with ffmpeg Support

1. Remove any pre-installed ffmpeg packages:

```sudo apt-get -qq remove x264 libx264-dev ffmpeg
sudo apt-get --purge remove libav-tools
sudo apt-get --purge autoremove
```
2. Install dependencies:

`sudo apt-get -qq install libopencv-dev build-essential checkinstall cmake pkg-config yasm libjpeg-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev python-dev python-numpy libtbb-dev libqt4-dev libgtk2.0-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils`
3. Install ffmpeg:

```git clone git://source.ffmpeg.org/ffmpeg.git ffmpeg
cd ffmpeg
./configure --enable-nonfree --enable-pic --enable-shared
make
sudo make install
```

4. Install OpenCV:

```git clone https://github.com/opencv/opencv.git opencv
cd opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_FFMPEG=ON ..
make -j2
sudo make install
```


### More Information

This repo is part of a bigger repo from TODO
