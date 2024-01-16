# Intro.-to-ML
NYCU 112 spring, lectured by 林彥宇

## HW1 - Linear regression with numpy (closed form solution & gradient descent)
## HW2 - Logistic regression & Fisher's linear discriminant with numpy
## HW3 - Decision tree & adaboost algorithm with numpy
## HW4 - Support vector machine with linear/polynomial/rbf kernel
## Final Project - Fine-grained image classification on bird
- source code cloned from [HERBS](https://github.com/chou141253/FGVC-HERBS)
- [Kaggle competition](https://www.kaggle.com/competitions/nycu2023mlfinalproject)
- rank: 1/111
- HERBS + ensemble(voting with confidence value)

![image](https://github.com/stanleyshen2003/Intro.-to-ML/assets/80504001/20f84815-f0b8-4319-9337-dbc3ec16932f)

### Training
I used some shell script to manipulate the training data. The shell scripts can be found in data_utils. 

You may want to modify configs/config.yaml
```bash
pip install -r requirements.txt
python3 main.py
```

### Inference
Check whether you put the images and config in the correct place.
```bash
pip install -r requirements.txt
python3 inference.py
```
