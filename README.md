# HERGAI

You will find herein the files related to our paper:

**Tran-Nguyen, V.K., Randriharimanamizara, U.F., Taboureau, O. HERGAI: An Artificial Intelligence Tool for Structure-Based Prediction of hERG Inhibitors. (2025)**

## Workflow

![Graphical-Abstract](https://github.com/vktrannguyen/HERGAI/blob/main/HERGAI_Computational_Workflow.png)

## HERGAI architecture

![Graphical-Abstract](https://github.com/vktrannguyen/HERGAI/blob/main/HERGAI_Diagram.png)

## Code

The code is stored in the **Code** folder:

- *HERGAI.ipynb*: the Jupyter notebook containing the Python code to train and test our base classification models (**RF_BC**, **XGB_BC**, **DNN_BC**) and our best stacking model (**DNN_SC**).
- *PLEC_extraction.py*: the Python code to extract PLEC fingerprints from receptor-bound docking poses of small molecules. These fingerprints are used as features for our base models.

## Data

All data are stored in the **Data** folder. Inside, you will find:

### The 'Training_set' sub-folder

- *training_data.csv*: the csv training data file containing 224,945 molecules in our training set. For each molecule, we provide its SID (PubChem substance identifier), activity (Active or Inactive), potency (-logIC50), and SMILES string.
- *training_ClassyPose.csv.zst*: the compressed csv file containing the "good pose probabilities" issued by ClassyPose for all docking poses of our training molecules.
- The **Stacking_ensemble_ML** sub-folder: you will find inside the following files:
  - *training_data_stackedML.csv*: the csv training data file specifically used for training our DNN_SC model (see our Jupyter notebook *HERGAI.ipynb*).
  - *rf_cv_predictions.csv*, *xgb_cv_predictions.csv*, *dnn_cv_predictions.csv*: the csv files containing the active probabilities and adjusted scores for all training molecules, specifically used for training our DNN_SC model (see our Jupyter notebook *HERGAI.ipynb*).

### The 'Test_set' sub-folder

- *test_data.csv*: the csv test data file containing 74,982 molecules in our test set. For each molecule, we provide its SID (PubChem substance identifier), activity (Active or Inactive), potency (-logIC50), and SMILES string.
- *test_3_base_models.csv*: the csv test data file specifically used for testing our DNN_SC model (see our Jupyter notebook *HERGAI.ipynb*).
- The **Results** sub-folder: you will find inside the following sub-folders:
  - The **Scores_All_poses** sub-folder: the csv files containing the scores issued by three existing scoring functions (Smina, RF-Score-VS, ClassyPose) for all docking poses of our test molecules.
  - The **Existing_SFs** sub-folder: the csv files containing all results from six virtual screening schemes involving existing scoring functions (Schemes 1-6, please read our article for more detail).
  - The **Our_AI_classifiers** sub-folder: the csv files containing all results from our six binary classifiers RF_BC, XGB_BC, DNN_BC, RF_SC, XGB_SC, and DNN_SC.

### The 'README.txt' file

This file contains the link to download the PLEC fingerprints extracted from hERG-bound docking poses of our training and test molecules, as selected by ClassyPose: *training_PLEC_ClassyPose.csv* and *test_PLEC_ClassyPose.csv*. These fingerprints are directly used as features for our base models.

### The 'HergSPred_predictions' sub-folder

- *true_negatives.smi* and *false_positives.smi*: the SMILES strings and SIDs of inactive molecules in the test set which are correctly labeled (true negatives) and incorrectly labeled (false positives) by our best model (DNN_SC).
- *HergSPred_output_TN_subset.csv* and *HergSPred_output_FP_subset.csv*: HergSPred predictions on the hERG inhibitory activity of a representative subset of true negatives (TN) and a representative subset of false positives (FP). Each subset corresponds to 1% of the TN or FP population contained in each smi file.

## Attention

To use our code, you need to install **Python (v.3.7)** and set up a proper environment beforehand. A suggested solution is to use the *protocol-env.yml* file provided in our **MLSF-protocol** GitHub repository (https://github.com/vktrannguyen/MLSF-protocol) and install a few additional packages (e.g., imblearn). Please refer to the **import** section at the beginning of each code block in our Jupyter notebook *HERGAI.ipynb* to ensure that all required Python dependencies are installed.

---------------------------------------------------------------------------------------------------------------------------------------------------

This work was carried out at the Unité de Biologie Fonctionnelle et Adaptative (BFA), INSERM U1133, CNRS UMR8251, Université Paris Cité, France. The latest version of all data and source code provided herein was updated and made available free of charge in January 2025, and is subject to copyright.




