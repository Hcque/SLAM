
#include <pcl/io/ply_io.h>
#include <pcl/io/vtk_lib_io.h>
#include <pcl/point_types.h>
#include <pcl/registration/icp.h>
#include <pcl/visualization/cloud_viewer.h>
#include <pcl/filters/filter_indices.h>
#include <pcl/common/transforms.h>

#include <vtkRenderWindow.h>
#include <vtkRendererCollection.h>
#include <vtkCamera.h>

#include "SingleThreadIcp.cpp"
#include "common.hpp"
#include "GoIcp.cpp"
#include "testLDT.cpp"

#include <time.h>
#include <cmath>
#include <fstream>


#include <omp.h>

using namespace icp;
using namespace std;

PointCloudTPtr cloud_source ,cloud_target;
Eigen::MatrixXd source_matrix, target_matrix;

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


MatrixXd pData, pTmp, pModel;
Matrix4d guess;


void icp(MatrixXd pData, Matrix pModel)
{
	pData = pData * guess;
	pTmp = pData;
	for (int i = 0; i < 5 ; i ++ )
	{

		// find corresp of pTmp with pModel

		// computer XYt

		U,S,V = svd(XYt);

		R = Vt* U
		if (det(V) == -1) {

		}
		t = f(R);
		Rt = f(R,t);
		pTmp = pTmp * Rt;
		guess *= Rt
	}
	// the ans = guess

}


const int NUM_PARTICLES = 10;
struct Particle
{
	double w;
	double x[6];
};
Particle para[NUM_PARTICLES];
Particle para_new[NUM_PARTICLES];
void init_particles()
{
	
}

// assume pData N * 3, has been centralized
void particle_Filter(MatrixXd pData, MatrixXd pModel)
{
	double xRange[2], yRange[2], zRange[2];
	rand()*1.0 / INT_MAX
	for (int j = 0; j < NUM_PARTICLES; j ++)
	{
		para[j].w = 1.0 / NUM_PARTICLES;
		para[j].x[0] = xRange[0] + rand();
		//TODO
	}

	// motion model
	for (int i = 0; i < 5; i ++)
	{
		// motion model, draw samples from mg
			mu, Sigma;
			mixture of Guassian;
		// recal weiht
		for (int j = 0; j < NUM_PARTICLES; j ++)
		{
			reassign x;
			para[j].w = f();
		}
		
		for (int j = 0; j < NUM_PARTICLES; j ++)
		{
			// redraw sample
			newpara[j] = 
		}

	}

}

double mse;


void _normal(PointCloudTPtr &cloud_target, int file = 0)
{
	fstream _file;
	_file.open("model.txt", ios::out);
	double _min_x = 1e9, _max_x = -1e9;
	double _min_y = 1e9, _max_y = -1e9;
	double _min_z = 1e9, _max_z = -1e9;
	double dia_x, dia_y, dia_z;

	if (file) _file << cloud_target->points.size() << "\n";
	for (int i = 0 ; i < cloud_target->points.size(); i ++ )
	{
		double x = cloud_target->points[i].x;
		if (x < _min_x) _min_x = x;
		if (x > _max_x) _max_x = x;
		double y = cloud_target->points[i].y;
		if (y < _min_y) _min_y = y;
		if (y > _max_y) _max_y = y;
		double z = cloud_target->points[i].z;
		if (z < _min_z) _min_z = z;
		if (z > _max_z) _max_z = z;
	}

	dia_x = (_min_x + _max_x) / 2;
	dia_y = (_min_y + _max_y) / 2;
	dia_z = (_min_z + _max_z) / 2;

	for (int i = 0 ; i < cloud_target->points.size(); i ++ )
	{
		double x = cloud_target->points[i].x;
		x = 0.0 + (x - dia_x)*1.0/ (_max_x-_min_x);
		double y = cloud_target->points[i].y;
		y = 0.0 + (y - dia_y)*1.0/ (_max_y-_min_y);
		double z = cloud_target->points[i].z;
		z = 0.0 + (z - dia_z)*1.0/ (_max_z-_min_z);
		cloud_target->points[i] = {x,y,z};
		if (file){
		_file << 
		cloud_target->points[i].x << " " << 
		cloud_target->points[i].y << " " << 
		cloud_target->points[i].z << "\n";
		}
	}
	_file.close();

}


LDT *ldt;

float _X, _Y, _Z;
int CORES_ ;

int main(int argc, char**argv)
{
    // if (argc != 4) 
    // {
    //     std::cerr << "./a input1 input2 iter" << "\n";
    //     return -1;
    // }
	std::cerr << "load..." << "\n";
    cloud_source  = PointCloudTPtr(new PointCloudT());
    cloud_target  = PointCloudTPtr(new PointCloudT());
    loadFile(argv[1], *cloud_source);
    loadFile(argv[2], *cloud_target);

	_normal(cloud_source, 0);
	_normal(cloud_target, 0);

	
	// particle filter
    
    return 0;
}
