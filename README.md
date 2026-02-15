# High-Resolution Leeds Sports Pose Extended Training Set (HR-LSPET)

**Authors:** Leonid Pishchulin, Mykhaylo Andriluka, Bernt Schiele

## Dataset Description

This dataset was created by re-downloading the original high-resolution images of the Leeds Sports Pose Extended Training Set (LSPET) from Flickr using the links provided by the authors. In total, the dataset contains 9,428 images; 572 out of 10,000 original images were not available at the time of download. Downloaded images were re-annotated by in-house workers and annotations were quality-controlled.

## File Structure

The file `joints.mat` contains 14 joint locations for each image along with a binary value specifying joint visibility.

### Joint Ordering

The joints are ordered as follows:

1. Right ankle
2. Right knee
3. Right hip
4. Left hip
5. Left knee
6. Left ankle
7. Right wrist
8. Right elbow
9. Right shoulder
10. Left shoulder
11. Left elbow
12. Left wrist
13. Neck
14. Head top

## Acknowledgements

If you use this dataset, please cite the following papers:

### [1] Learning Effective Human Pose Estimation from Inaccurate Annotation

**Authors:** Sam Johnson and Mark Everingham  
**Conference:** IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2011

```bibtex
@inproceedings{Johnson11,
   title = {Learning Effective Human Pose Estimation from Inaccurate Annotation},
   author = {Johnson, Sam and Everingham, Mark},
   year = {2011},
   booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)}
}
```

### [2] DeepCut: Joint Subset Partition and Labeling for Multi Person Pose Estimation

**Authors:** Leonid Pishchulin, Eldar Insafutdinov, Siyu Tang, Bjoern Andres, Mykhaylo Andriluka, Peter Gehler, Bernt Schiele  
**Conference:** IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2016

```bibtex
@inproceedings{pishchulin16cvpr,
   title = {DeepCut: Joint Subset Partition and Labeling for Multi Person Pose Estimation},
   booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
   year = {2015},
   author = {Leonid Pishchulin and Eldar Insafutdinov and Siyu Tang and Bjoern Andres and Mykhaylo Andriluka and Peter Gehler and Bernt Schiele}
}
```

## Contact

If you have any questions, please contact Leonid Pishchulin at leonid@mpi-inf.mpg.de

