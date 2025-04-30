from wine_quality_predictor import logger
from wine_quality_predictor.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from wine_quality_predictor.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from wine_quality_predictor.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from wine_quality_predictor.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from wine_quality_predictor.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f"\n\n{'*'*20} {STAGE_NAME} {'*'*20}\n")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"\n\n{'*'*20} {STAGE_NAME} completed {'*'*20}\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"


try:
    logger.info(f"\n\n{'*'*20} {STAGE_NAME} {'*'*20}\n")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f"\n\n{'*'*20} {STAGE_NAME} completed {'*'*20}\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"


try:
    logger.info(f"\n\n{'*'*20} {STAGE_NAME} {'*'*20}\n")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"\n\n{'*'*20} {STAGE_NAME} completed {'*'*20}\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer Stage"


try:
    logger.info(f"\n\n{'*'*20} {STAGE_NAME} {'*'*20}\n")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f"\n\n{'*'*20} {STAGE_NAME} completed {'*'*20}\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f"\n\n{'*'*20} {STAGE_NAME} {'*'*20}\n")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f"\n\n{'*'*20} {STAGE_NAME} completed {'*'*20}\n")
except Exception as e:
    logger.exception(e)
    raise e