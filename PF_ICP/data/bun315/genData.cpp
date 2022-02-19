


#include <pcl/io/ply_io.h>
#include <pcl/io/vtk_lib_io.h>
#include <pcl/point_types.h>
#include <pcl/registration/icp.h>
#include <pcl/visualization/cloud_viewer.h>
#include <pcl/filters/filter_indices.h>
#include <pcl/common/transforms.h>


#include <time.h>
#include <cmath>
#include <fstream>



#include <iostream>
#include <cmath>
#include <Eigen/Core>
#include <pcl/common/common.h>


    int NUM_TH = 1;
#define SQ(x) ((x)*(x))

using IndexT = uint32_t;
#define INVALID_INDEX IndexT(-1)

using Vector3f = Eigen::Vector3f;
using Vector3d = Eigen::Vector3d;
using Vector3i = Eigen::Vector3i;

using Matrix3f = Eigen::Matrix3f;
using Matrix4f = Eigen::Matrix4f;
using Matrix4d = Eigen::Matrix4d;
using Matrix3d = Eigen::Matrix3d;

using Point3f = pcl::PointXYZ;
using PointCloudT = pcl::PointCloud<Point3f>;
using PointCloudTPtr = pcl::PointCloud<Point3f>::Ptr;


using namespace std;

PointCloudTPtr cloud_source ,cloud_target;

clock_t clockBegin, clockEnd;


void loadFile(const char* file_name, PointCloudT &cloud)
{
	pcl::PolygonMesh mesh;

	if(pcl::io::loadPolygonFile(file_name, mesh)==-1)
	{
		PCL_ERROR("File loading faild.");
		return;
	}
	else
	{
		pcl::fromPCLPointCloud2<Point3f>(mesh.cloud, cloud);
	}

	std::vector<int> index;
	pcl::removeNaNFromPointCloud(cloud, cloud, index);
}


int Nd, Nm;


int main(int argc, char**argv)
{
   
	std::cerr << "load..." << "\n";
    cloud_source  = PointCloudTPtr(new PointCloudT());
    cloud_target  = PointCloudTPtr(new PointCloudT());
    loadFile(argv[1], *cloud_source);
    loadFile(argv[2], *cloud_target);

    Nd = cloud_source->points.size();
    Nm = cloud_target->points.size();









}
