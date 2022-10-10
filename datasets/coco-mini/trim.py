from operator import contains
import os
import random
import json
import sys

def trim_data(dir_to_trim, retainment):
    for file in os.listdir(dir_to_trim):
        cut_val = random.random()
        if cut_val > retainment:
            os.remove(f"{dir_to_trim}/{file}")

def correct_annotations(dir_to_trim):
    for file in os.listdir("annotations"):
        if not contains(file, dir_to_trim):
            continue
        with open(f"annotations/{file}", 'r') as f:
            ann_data = json.load(f)
            count = 0
            new_imgs = []
            new_anns = []
            ids = set()
            for i in range(len(ann_data["images"])):
                if ann_data["images"][i]["file_name"] in os.listdir(dir_to_trim):
                    new_imgs.append(ann_data["images"][i])
                    ids.add(ann_data["images"][i]["id"])
                    count += 1
            for i in range(len(ann_data["annotations"])):
                if ann_data["annotations"][i]["image_id"] in ids:
                    new_anns.append(ann_data["annotations"][i])
            ann_data["images"] = new_imgs
            ann_data["annotations"] = new_anns
            with open(f"annotations/new-{file}", 'w') as new_f:
                json.dump(ann_data, new_f)
            print(f"new-{file} now acknowledges new sample count of: {count}")

def replace_old_annotations():
    for file in os.listdir("annotations"):
        if file.startswith("new-"):
            file = "annotations/" + file
            os.remove(file.replace("new-", ""))
            os.rename(file, file.replace("new-", ""))
    print("All old annotation JSONs replaced with new versions")

def main():
    if len(sys.argv) != 3:
        sys.exit("Error: Must have exactly two arguments: <data_type_to_trim> <amount_to_retain>")
    to_trim = sys.argv[1].lower()
    if to_trim == "train":
        dir_to_trim = "train2017"
    elif to_trim == "val":
        dir_to_trim = "val2017"
    else:
        sys.exit("Error: arg <data_type_to_trim> must be one of 'train' or 'val'")
    try:
        retainment = float(sys.argv[2])
        if retainment < 0 or retainment > 1:
            raise Exception
    except Exception:
        sys.exit("Error: arg <amount_to_retain> must be a float value [0,1]")

    print(f"Current # of samples: {len(os.listdir(dir_to_trim))}, will retain ~{retainment*100}%")
    trim_data(dir_to_trim, retainment)
    correct_annotations(dir_to_trim)
    replace_old_annotations()

if __name__ == "__main__":
    main()
