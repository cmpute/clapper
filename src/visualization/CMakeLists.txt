cmake_minimum_required(VERSION 2.8.3)
project(zzz_visualization)

find_package(catkin REQUIRED)
catkin_package()

catkin_python_setup()

catkin_install_python(PROGRAMS
  nodes/detection
  nodes/detection2d
  nodes/semantics
  nodes/tracking
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
