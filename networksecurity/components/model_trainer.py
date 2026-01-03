import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.entity.artifact_entity import DataTransformationArtifacts,ModelTrainerArtifacts,ClassificationMetricArtifacts
from networksecurity.constant import training_pipeline


from networksecurity.utlis.main_utils.utlis import ( save_object,load_object,
                                    load_numpy_array_data , evaluate_models)
from networksecurity.utlis.ml_utils.metric.classification_metric import get_classification_score
from networksecurity.utlis.ml_utils.model.estimator import NetworkModel

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import(
    AdaBoostClassifier,
    RandomForestClassifier,
    GradientBoostingClassifier,
)
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
import mlflow

if os.getenv("ENABLE_DAGSHUB", "false").lower() == "true":
    import dagshub
    dagshub.init(repo_owner='Korale05', repo_name='NetworkSecurity', mlflow=True)




class ModelTrainer:
    def __init__(self,model_trainer_config : ModelTrainerConfig,data_transformation_artifacts : DataTransformationArtifacts):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifacts = data_transformation_artifacts
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def track_mlflow(self,best_model,classificationmetric,best_model_name):
        with mlflow.start_run(run_name=best_model_name):
            f1_score = classificationmetric.f1_score
            precision_score = classificationmetric.precision_score
            recall_score = classificationmetric.recall_score

            mlflow.log_metric("f1_score",f1_score)
            mlflow.log_metric("precision",precision_score)
            mlflow.log_metric("recall score",recall_score)
            mlflow.sklearn.log_model(best_model,"model")



    def train_model(self,x_train,y_train,x_test,y_test):
        try:
            models = {
            "Random Forest" : RandomForestClassifier(verbose=1),
            "Decision Tree" : DecisionTreeClassifier(),
            "Gradient Boosting" : GradientBoostingClassifier(verbose=1),
            "Logistics Regression" : LogisticRegression(verbose=1),
            "Ada boost" : AdaBoostClassifier(),
            "Kneighbours" : KNeighborsClassifier(),
            "XGB classifier" : XGBClassifier(),
            "CatBoostClassifier" : CatBoostClassifier(verbose=1)
            }
            params = {

                "Random Forest": {
                    "n_estimators": [100, 300, 500],
                    "criterion": ["gini", "entropy", "log_loss"],
                    "max_depth": [None, 10, 20, 30, 50],
                    "min_samples_split": [2, 5, 10],
                    "min_samples_leaf": [1, 2, 5],
                    "max_features": ["sqrt", "log2", None],
                    "bootstrap": [True, False],
                    "class_weight": [None, "balanced"]
                },

                "Decision Tree": {
                    "criterion": ["gini", "entropy", "log_loss"],
                    "max_depth": [None, 5, 10, 20, 50],
                    "min_samples_split": [2, 5, 10],
                    "min_samples_leaf": [1, 2, 5],
                    "max_features": [None, "sqrt", "log2"],
                    "splitter": ["best", "random"],
                    "class_weight": [None, "balanced"]
                },

                "Gradient Boosting": {
                    "n_estimators": [100, 200, 300],
                    "learning_rate": [0.01, 0.05, 0.1],
                    "subsample": [0.6, 0.8, 1.0],
                    "max_depth": [2, 3, 5],
                    "min_samples_split": [2, 5, 10],
                    "min_samples_leaf": [1, 2, 5],
                    "max_features": ["sqrt", "log2", None]
                },

                "Logistics Regression": {
                    "penalty": ["l1", "l2", "elasticnet", None],
                    "C": [0.001, 0.01, 0.1, 1, 10],
                    "solver": ["liblinear", "lbfgs", "saga", "newton-cholesky"],
                    "class_weight": [None, "balanced"],
                    "l1_ratio": [0, 0.5, 1]
                },

                "Ada boost": {
                    "n_estimators": [50, 100, 200, 300],
                    "learning_rate": [0.01, 0.05, 0.1, 1],
                    "algorithm": ["SAMME", "SAMME.R"]
                },

                "Kneighbours": {
                    "n_neighbors": [3, 5, 7, 9, 15],
                    "weights": ["uniform", "distance"],
                    "metric": ["minkowski", "manhattan", "euclidean"],
                    "p": [1, 2]
                },

                "XGB classifier": {
                    "n_estimators": [200, 400, 600],
                    "learning_rate": [0.01, 0.05, 0.1],
                    "max_depth": [3, 5, 7, 10],
                    "subsample": [0.6, 0.8, 1.0],
                    "colsample_bytree": [0.6, 0.8, 1.0],
                    "gamma": [0, 1, 5],
                    "reg_alpha": [0, 0.1, 1],
                    "reg_lambda": [1, 5, 10],
                    "min_child_weight": [1, 3, 5]
                },

                "CatBoostClassifier": {
                    "iterations": [300, 500, 800],
                    "learning_rate": [0.01, 0.03, 0.1],
                    "depth": [3, 5, 7, 10],
                    "l2_leaf_reg": [1, 3, 5, 7],
                    "border_count": [32, 64, 128],
                    "bagging_temperature": [0, 1, 5],
                    "random_strength": [1, 2, 5]
                }
            }
            models_report : dict = evaluate_models(x_train,y_train,x_test,y_test,models,params)

            # To get best model score from dict
            best_model_score = max(sorted(models_report.values()))

            # To get the best model name from dict

            best_model_name = list(models_report.keys())[
                list(models_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]


            y_train_pred = best_model.predict(x_train)
            classification_train_matric = get_classification_score(y_true=y_train,y_pred=y_train_pred)
            ##Track the expriment with mlflow of train matrix
            self.track_mlflow(best_model,classification_train_matric,best_model_name)


            y_test_pred = best_model.predict(x_test)
            classification_test_matric = get_classification_score(y_true=y_test,y_pred=y_test_pred)
            ##Track the expriment with mlflow of test matrix
            self.track_mlflow(best_model,classification_test_matric,best_model_name)

            preprocessor = load_object(file_path=self.data_transformation_artifacts.transformed_object_file_path)

            model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
            os.makedirs(model_dir_path,exist_ok=True)

            Network_Model = NetworkModel(preprocessor=preprocessor,model=best_model)

            save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=Network_Model)

            save_object("final_model/model.pkl",best_model)
            
            #Model trainer Artifacts
            model_trainer_artifact = ModelTrainerArtifacts(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                train_metric_artifacts=classification_train_matric,
                test_metric_artifacts=classification_test_matric
            )
            logging.info(f"Model trainer artifact : {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
         

    def initiate_model_trainer(self)->ModelTrainerArtifacts:
        try:
            train_file_path = self.data_transformation_artifacts.transformed_train_file_path
            test_file_path = self.data_transformation_artifacts.transformed_test_file_path
            logging.info("taking train and test file path from data_trainsformation_artifacts")

            logging.info("Loading the train and test to numpy array")
            #loading training arrya and testing array
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            #split the train to x_train,y_train and test to x_test,y_test
            logging.info("split the train to x_train,y_train and test to x_test,y_test")
            x_train,y_train,x_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            model_trainer_artifacts = self.train_model(x_train,y_train,x_test,y_test)
            return model_trainer_artifacts

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
