High-Resolution Leeds Sports Pose Extended Training Set (HR-LSPET)
Leonid Pishchulin, Mykhaylo Andriluka, Bernt Schiele

This dataset was created by re-downloading the original
high-resolution images of the Leeds Sports Pose Extended Training Set
(LSPET) [1] from Flickr using the links provided by the authors. In
total the dataset contains 9,428 images, 572 out of 10,000 original
images were not available at the time of download. Downloaded images
were re-annotated by in-house workers and annotations were
quality-controlled.

File 'joints.mat' contains 14 joint locations for each image along
with a binary value specifying joint visibility.

The ordering of joints is as follows:

Right ankle
Right knee
Right hip
Left hip
Left knee
Left ankle
Right wrist
Right elbow
Right shoulder
Left shoulder
Left elbow
Left wrist
Neck
Head top

If you use this dataset, please cite [1,2]

[1] Sam Johnson and Mark Everingham.
    "Learning Effective Human Pose Estimation from Inaccurate Annotation".
    In IEEE Conference on Computer Vision and Pattern Recognition(CVPR)
    2011

@inproceedings{Johnson11,
   title = {Learning Effective Human Pose Estimation from Inaccurate
   Annotation},
   author = {Johnson, Sam and Everingham, Mark},
   year = {2011},
   booktitle = {IEEE Conference on Computer Vision and
   Pattern Recognition (CVPR)}
}

[2] Leonid Pishchulin, Eldar Insafutdinov, Siyu Tang, Bjoern Andres,
    Mykhaylo Andriluka, Peter Gehler, Bernt Schiele.
    "DeepCut: Joint Subset Partition and Labeling for Multi Person Pose Estimation"
    In IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
    2016

@inproceedings{pishchulin16cvpr,
        title = {DeepCut: Joint Subset Partition and Labeling for
        Multi Person Pose Estimation},
        booktitle = {IEEE Conference on Computer Vision and
   	Pattern Recognition (CVPR)},
        year = {2015},
	author = {Leonid Pishchulin and Eldar Insafutdinov and Siyu
        Tang and Andres, Bjoern and Mykhaylo Andriluka and Peter
        Gehler and Bernt Schiele}
}

If you have any questions, please contact Leonid Pishchulin at
leonid@mpi-inf.mpg.de
