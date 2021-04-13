from django.shortcuts import render
from django.http import HttpResponse
import joblib

model = joblib.load('breast_cancer_1.pkl')
# Create your views here.

def home(request):
	return  HttpResponse('This is homep page!! ')


def cancer(request):
	return  render(request,'bcancer/cancer_data.html')


def cancer_predict(request):

	lis=[]

	lis.append(request.GET['radius_mean'])
	lis.append(request.GET['texture_mean'])	
	lis.append(request.GET['perimeter_mean'])
	lis.append(request.GET['area_mean'])
	lis.append(request.GET['smoothness_mean'])
	lis.append(request.GET['compactness_mean'])	
	lis.append(request.GET['concavity_mean'])
	lis.append(request.GET['concave_points_mean'])
	lis.append(request.GET['symmetry_mean'])
	lis.append(request.GET['fractal_dimension_mean'])	
	lis.append(request.GET['radius_se'])
	lis.append(request.GET['texture_se'])
	lis.append(request.GET['perimeter_se'])
	lis.append(request.GET['area_se'])
	lis.append(request.GET['smoothness_se'])
	lis.append(request.GET['compactness_se'])
	lis.append(request.GET['concavity_se'])
	lis.append(request.GET['concave_points_se'])	
	lis.append(request.GET['symmetry_se'])
	lis.append(request.GET['fractal_dimension_se'])
	lis.append(request.GET['radius_worst'])
	lis.append(request.GET['texture_worst'])
	lis.append(request.GET['perimeter_worst'])
	lis.append(request.GET['area_worst'])
	lis.append(request.GET['smoothness_worst'])
	lis.append(request.GET['compactness_worst'])
	lis.append(request.GET['concavity_worst'])
	lis.append(request.GET['concave_points_worst'])
	lis.append(request.GET['symmetry_worst'])
	lis.append(request.GET['fractal_dimension_worst'])

	final_result =model.predict([lis])
	print(final_result[0])

	if final_result[0]== 0:
		final_result='Yes'
	else:
		final_result='No'

	context ={
	'final_result': final_result

	}

	return  render(request,'bcancer/cancer_data.html',context)	


