import data_preprocessing
import data_processing
import aggregate_in_csv
import data_postprocessing


def engine(directory, are_you_bored=False):
    warehouse = data_preprocessing.pre_process(directory)
    keys = list(warehouse.keys())
    output = {}
    for i in warehouse.keys():
        res = data_processing.process_data(warehouse[i])
        print('Processing -> ' + i)
        output[i] = res
    res = data_postprocessing.post_process(output)
    aggregate_in_csv.write_in_csv(res, are_you_bored)
