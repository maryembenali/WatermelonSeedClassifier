# WatermelonSeedClassifier
### Project context:
The Watermelon Seed Classifier project is a result of the Validation of Conception and Development project module at ENSI School for the second semester of the second year. </br> </br>
<p align="center"> <img width=120 src="https://ensi.rnu.tn/stylesheets/images/header/header_logo.png" alt="Engineering School of Computer Science Logo "> </p>  </br> </br>

This project is proposed by the R&D Department of Limagrain Group, under the guidance of ** Mr. Ali Boudjedra ** the R&D Senior Project Leader in Artificial Vision, AI & Automation.

### About the host organization:
<p align="center"> <img width=200 src="https://www.limagrain.com/assets/front/img/fr/logo-limagrain-3.svg" alt="Limagrain 's Logo "> </p>  </br> </br>

[Limagrain Group](https://www.limagrain.com/) is a renowned international agricultural cooperative specializing in plant breeding and seed production. With a rich history spanning several decades, Limagrain has established itself as a leading global player in the seed industry. Their commitment to innovation and sustainable agriculture has led them to explore cutting-edge technologies, including artificial vision and AI, to enhance seed-related processes and deliver high-quality agricultural solutions.

## Environment dependencies </br>
### Modeling
For the modeling phase , you need to create a seperate environment on anaconda different from the base env:
- Python 3.7.16
- libraries : </br>
              - tensorflow Version: 2.10.0</br>
              - matplotlib Version: 3.5.2</br>
              - numpy Version: 1.21.5</br>
              - sk learn Version: 1.0.2 ( for the ml approch)</br>

### GUI
To view the GUI first you need to : <br />
1. Download streamlit in your work environment ; can be the base env ( it should contain Python version 3.9.13 ) <br />
streamlit Version: 1.21.0

2. Download this streamlit component <br />
```
pip install st-pages 
``` 
in your work environment : you can view its documentation through [this link](https://github.com/blackary/st_pages ) <br />
3. Join the model.h5 file in the folder containing all the files of the main branch  locally as it was too heavy to be uploaded on github <br />
4. To run the app : - streamlit run Complete_Path/app.py <br />

pandas Version: 1.4.4 <br />
numpy Version: 1.23.5 <br />
PIL <br />
Plotly Version: 5.9.0 <br />
