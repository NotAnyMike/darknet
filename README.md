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

* For single images: TODO
* For video:

	1. cd into EUFS: `cd EUFS`
	2. run the command: `./darknet detector demo cfg/cones-obj.data cfg/cones-obj.cfg weights/v1/yolo-cones_2000.weights -thresh 0.25 videos/out.mp4`

* For several images

## How to retrain it

TODO

## Weights

| name | description |
| --- | --- |
| `darknet19_448.conv.23` | original from yolo used in retraining |
| `v1/...2000.weights` | **Stable weights** for cones |

## Extra information

This repo is part of a bigger repo from TODO
