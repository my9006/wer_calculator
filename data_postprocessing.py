def post_process(output_dict):
    list_of_lists = []
    for item in output_dict.keys():
        list_item = [item, output_dict[item]['wer'], output_dict[item]['wer']]
        list_of_lists.append(list_item)
    return list_of_lists
