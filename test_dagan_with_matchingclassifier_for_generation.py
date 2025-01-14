
from generation_builder_with_matchingclassifier_finalversion import ExperimentBuilder
from utils.parser_util import get_args

batch_size, num_gpus ,support_num, args = get_args()
# set the data provider to use for the experiment



if args.is_all_test_categories > 0:
    ###### generating images for all test categories
    import data_with_matchingclassifier_for_quality_and_classifier_finalversion as dataset
else:
    ###### generating images for those selected categories
    import data_for_selecteddata_for_generation as dataset




if args.dataset == 'omniglot':
    print('omniglot')
    data = dataset.OmniglotDAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                        num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num
                                        ,is_training=args.is_training
                                        ,general_classification_samples=args.general_classification_samples
                                        ,selected_classes=args.selected_classes, image_size=args.image_width)

elif args.dataset == 'vggface':
    print('vggface')
    data = dataset.VGGFaceDAGANDataset(batch_size=batch_size, last_training_class_index=1600, reverse_channels=True,
                                       num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num
                                       ,is_training=args.is_training
                                       ,general_classification_samples=args.general_classification_samples
                                       ,selected_classes=args.selected_classes ,image_size=args.image_width)

elif args.dataset == 'miniimagenet':
    print('miniimagenet')
    data = dataset.miniImagenetDAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                            num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num
                                            ,is_training=args.is_training
                                            ,general_classification_samples=args.general_classification_samples
                                            ,selected_classes=args.selected_classes ,image_size=args.image_width)

elif args.dataset == 'emnist':
    print('emnist')
    data = dataset.emnistDAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                      num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num
                                      ,is_training=args.is_training
                                      ,general_classification_samples=args.general_classification_samples
                                      ,selected_classes=args.selected_classes ,image_size=args.image_width)

elif args.dataset == 'figr':
    print('figr')
    data = dataset.FIGRDAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                    num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num
                                    ,is_training=args.is_training
                                    ,general_classification_samples=args.general_classification_samples
                                    ,selected_classes=args.selected_classes ,image_size=args.image_width)
elif args.dataset == 'fc100':
    data = dataset.FC100DAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                     num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num
                                     ,is_training=args.is_training
                                     ,general_classification_samples=args.general_classification_samples
                                     ,selected_classes=args.selected_classes ,image_size=args.image_width)
elif args.dataset == 'animals':
    data = dataset.animalsDAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                       num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num
                                       ,is_training=args.is_training
                                       ,general_classification_samples=args.general_classification_samples
                                       ,selected_classes=args.selected_classes ,image_size=args.image_width)

elif args.dataset == 'flowers':
    data = dataset.flowersDAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                       num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num
                                       ,is_training=args.is_training
                                       ,general_classification_samples=args.general_classification_samples
                                       ,selected_classes=args.selected_classes ,image_size=args.image_width)
elif args.dataset == 'SelectMOREanimals':
    data =  dataset.SelectMOREanimalsDAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                        num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num,is_training=args.is_training,general_classification_samples=args.general_classification_samples,selected_classes=args.selected_classes,image_size=args.image_width)



elif args.dataset == 'flowersselected':
    data = dataset.flowersselectedDAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                               num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num
                                               ,is_training=args.is_training
                                               ,general_classification_samples=args.general_classification_samples
                                               ,selected_classes=args.selected_classes ,image_size=args.image_width)


elif args.dataset == 'birds':
    data = dataset.birdsDAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                     num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num
                                     ,is_training=args.is_training
                                     ,general_classification_samples=args.general_classification_samples
                                     ,selected_classes=args.selected_classes ,image_size=args.image_width)

elif args.dataset == 'birds':
    data = dataset.birdsDAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                        num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num,is_training=args.is_training,general_classification_samples=args.general_classification_samples,selected_classes=args.selected_classes,image_size=args.image_width)
elif args.dataset == 'nabirds':
    data = dataset.NAbirdsDAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                        num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num,is_training=args.is_training,general_classification_samples=args.general_classification_samples,selected_classes=args.selected_classes,image_size=args.image_width)

elif args.dataset == 'food':
    data = dataset.FoodDAGANDataset(batch_size=batch_size, last_training_class_index=900, reverse_channels=True,
                                        num_of_gpus=num_gpus, gen_batches=1000, support_number=support_num,is_training=args.is_training,general_classification_samples=args.general_classification_samples,selected_classes=args.selected_classes,image_size=args.image_width)



# init experiment
experiment = ExperimentBuilder(args, data=data)
# run experiment
experiment.run_experiment()

