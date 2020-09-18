The web app can be found at http://104.154.194.125

# Dog-Breed
A dog-breed classifier using the Stanford Dog Breed dataset.
The model uses transfer learning and uses the pre trained weights of the inception model.
Additional layers are added over the inception layer to reduce training time and to get better results as the inception network is already trained on a huge dataset.

![Dog Breeds](https://user-images.githubusercontent.com/26468713/34918645-fbfe6bc2-f97b-11e7-9f89-548b508db905.jpg)

# DATASET
The Stanford Dogs dataset contains images of 120 breeds of dogs from around the world. This dataset has been built using images and annotation from ImageNet for the task of fine-grained image categorization. Contents of this dataset:

* Number of categories: 120
* Number of images: 20,580
* Annotations: Class labels, Bounding boxes

The dataset can be found at: *http://vision.stanford.edu/aditya86/ImageNetDogs/*

# Training
The model uses transefer learning and uses the pre trained weights of the inception model.
Additional layers are added over the inception layer to reduce training time and to get better results as the inception network is already trained on a huge dataset.
* For the first model a single GlobalAveragePooling layer is added between the inception model and the output layer.
* In the second model multiple dense layers with dropout layer is added between the inception model and the output layer.

Validation accuracy of around **80%** is achieved for the final model.

# Web-App
The web-app is designed on Streamlit and deployed using GCP
It can be found at http://104.154.194.125

# Conclusion
* Many more layers are needed over the transfer model as they were not designed on that specific task.
* Inception model trained on the ImageNet dataset helps us in achieving the results at a faster pace.
