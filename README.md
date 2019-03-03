<span style="color:red">This version is adapted for the EUFS team</span>

# YOLO for cone detections

TODO: small description of this repo and some of its output videos and images 

## How to install it

1. Modify `MakeFile` depending on your system
1. Compile it using `make`

## How to install it to use video 

1. Install opencv for ubuntu (not using pip or conda)

## How to run it

TODO: small description

* For single images: 

	1. cd into EUFS: `cd EUFS`
	2. run the command: `./darknet detector test cfg/cones-obj.data cfg/cones-obj.cfg <<path to weights file>> -i 0 -thresh 0.25 <<path to image>>`

	For example: `./darknet detector test cfg/cones-obj.data cfg/cones-obj.cfg weights/v1/yolo-cones_2000.weights -i 0 -thresh 0.25 cones/frame0030.jpg`

	NOTE: The command saves the images with predictions in the `EUFS` directory as `predictions.jpg`

* For video:

	1. cd into EUFS: `cd EUFS`
	2. run the command: `./darknet detector demo cfg/cones-obj.data cfg/cones-obj.cfg <<path to weight file>> -thresh 0.25 <<path to video file>>`

	For example: `./darknet detector demo cfg/cones-obj.data cfg/cones-obj.cfg weights/v1/yolo-cones_2000.weights -thresh 0.25 videos/out.mp4`

* For several images


NOTE: `tresh` flag is the minimum treshold of confidence for the prediction
## How to retrain it

TODO

## Weights

| name | description |
| --- | --- |
| `darknet19_448.conv.23` | original from yolo used in retraining |
| `v1/...2000.weights` | **Stable weights** for cones |

## Extra information

This repo is part of a bigger repo from TODO
