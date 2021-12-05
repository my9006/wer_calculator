import csv
import joke_requester as jr


def write_in_csv(data, are_you_bored):
    with open("./output/wer_levenstein_result.csv", mode='w+', newline='') as csv_file:
        headers = ["Test Case", "WER", "Levenstein distance"]
        if are_you_bored:
            headers.append("Dark humor for you")
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        for i in data:
            if are_you_bored:
                i.append(jr.request_joke())
            writer.writerow(i)
