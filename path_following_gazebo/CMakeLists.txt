cmake_minimum_required(VERSION 2.8.3)
project(path_following_gazebo)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  actionlib
  dbw_mkz_msgs
  geometry_msgs
  nav_msgs
)

catkin_package(
  CATKIN_DEPENDS dbw_mkz_msgs geometry_msgs nav_msgs roscpp rospy sensor_msgs
)

include_directories(
 include
  ${catkin_INCLUDE_DIRS}
)

include_directories(src/Eigen-3.3)
include_directories(/usr/local/include)
link_directories(/usr/local/lib)

add_library(mpc
  src/MPC.cpp
)
target_link_libraries(mpc
  ipopt
)

#${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
# target_link_libraries(${PROJECT_NAME}_node
#   ${catkin_LIBRARIES}
# )


add_executable(path_follower src/path_following.cpp)

target_link_libraries(path_follower
  ${catkin_LIBRARIES}
  mpc
)
