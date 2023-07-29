# WatermelonSeedClassifier
### Project context
The Watermelon Seed Classifier project is a result of the Validation of Conception and Development project module at ENSI School for the second semester of the second year. </br> </br>
<p align="center"> <img width=120 src="https://ensi.rnu.tn/stylesheets/images/header/header_logo.png" alt="Engineering School of Computer Science Logo "> </p>  </br> </br>

This project is proposed by the R&D Department of Limagrain Group, under the guidance of **Mr. Ali Boudjedra** the R&D Senior Project Leader in Artificial Vision, AI & Automation.

### About the host organization
<p align="center"> <img width=200 src="https://www.limagrain.com/assets/front/img/fr/logo-limagrain-3.svg" alt="Limagrain 's Logo "> </p>  </br> </br>

[Limagrain Group](https://www.limagrain.com/) is a renowned international agricultural cooperative specializing in plant breeding and seed production. With a rich history spanning several decades, Limagrain has established itself as a leading global player in the seed industry. Their commitment to innovation and sustainable agriculture has led them to explore cutting-edge technologies, including artificial vision and AI, to enhance seed-related processes and deliver high-quality agricultural solutions.
## Problematic

The watermelon production industry is rapidly expanding and becoming increasingly favored for its profitability. Seedless watermelons are particularly sought after for their convenience, reduced risk of injury for children and the elderly, longer shelf life, smoother texture, and sweeter flavor compared to seeded varieties.

However, obtaining seedless watermelons presents challenges due to their tendency to be triploid (3n chromosomes). To address this, pollination between diploid and tetraploid plants is used to produce triploid watermelons. 
<p align="center"> <img width=600 src="Image1.png" alt="pollination between diploid and tetraploid plants">

Infact the fruit of this pollination is a watermelon with seeds that gives later 3n watermelons.
|                                                                                                             |                                                                                                 |
| ------------------------------------------------------------------------------------------------------------| ----------------------------------------------------------------------------------------------- |
| <p> <img width=375 src="Image2.png" alt="fruit of a pollination between diploid and tetraploid plants"> </p>|  <p> <img width=400 src="Image3.png" alt="a fruit of the collected seeds "> </p> |

</br>
The self-pollinating nature of triploid watermelons introduces uncertainty in seed classification since tetraploid plants can pollinate themselves giving seeds of 4n watermelons later , making it difficult to differentiate between triploid and tetraploid seeds. </br>

### Goal 
Our project aims to develop an automated computer tool using machine learning techniques to classify watermelon seeds as triploid or tetraploid, assisting experts in the process. The developed models will classify individual seeds independently, irrespective of surrounding seeds or external factors, providing a time-efficient and accurate seed selection process.
## Needs Analysis
### Actors
Seed Technologist team in **Limagrain**
### Functional Needs
1. Read X-ray Images: The system reads X-ray images of watermelon seeds for analysis.
2. Classify Seeds: The tool classifies watermelon seeds as triploid or tetraploid.
3. Visualize Analysis Results: The results of the seed classification analysis are presented in a clear and accessible manner with a statistical chart.
4. Save Data: The analyzed data, including classification results and related information, can be saved for future reference.

### Non-Functional Needs 
1. Accuracy: 
2. Reliability: 
3. Speed: 
4. Robustness: 
5. User-Friendly: 
6. Scalability:
## Implementation
### Data Understanding
The dataset comprises the following components:
- 2068 X-ray Images: These images capture the internal structures of watermelon seeds and serve as the primary input for the classification process. The images are grouped into six separate directories for organization.
- Metadata Excel File: The accompanying Excel file contains essential metadata corresponding to the X-ray images. This metadata may include seed IDs, dimensions, weight, and other relevant information.
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
