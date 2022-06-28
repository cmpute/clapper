#!/usr/bin/env python

'''
This file transform the point cloud from the roadside sensor with precalculated rotation
'''

REPORT_POSE = False
objects_output_topic = "/velodyne_points_transformed"
input_topic = "/velodyne_points"
plane_coeffs = [-0.1448109745979309, -0.14773410558700562, 0.9783682227134705, 4.116767406463623] # this should be derived from the RANSAC estimation of the ground plane

import pcl
import rospy
import numpy as np
from scipy.spatial.transform import Rotation
from sensor_msgs.msg import PointCloud2

def handler(msg, pub):
    cloud = pcl.PointCloud(msg)

    if REPORT_POSE:
        # the source code for plane_ransac can be found at https://gist.github.com/cmpute/256a4676f753188f77416f94f21ee029
        import plane_ransac
        best_inliers, best_coeff = plane_ransac.plane_ransac(cloud.xyz)
        abc, d = best_coeff
        abc = np.asarray(abc)
        if d < 0: # normalize sign
            abc, d = -abc, -d
        print("Pose:", abc.tolist() + [d], ", inliers:", np.sum(best_inliers))

    if plane_coeffs:
        rot, _ = Rotation.align_vectors([[0, 0, 1]], [plane_coeffs[:3]])
        xyz = cloud.xyz.dot(rot.as_matrix().T)
        xyz[:, 2] += plane_coeffs[3]
        cloud.xyz = xyz

    # publish result
    new_msg = cloud.to_msg()
    new_msg.header = msg.header
    new_msg.header.frame_id = msg.header.frame_id + "_aligned"
    pub.publish(new_msg)

if __name__ == "__main__":
    rospy.init_node("roadside_transform")
    publisher = rospy.Publisher(objects_output_topic, PointCloud2, queue_size=1)
    subscriber = rospy.Subscriber(input_topic, PointCloud2, handler, publisher)
    rospy.loginfo("Node initialized.")
    rospy.spin()
