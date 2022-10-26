"""
Необходимо найти каждую метадату (файл формата .json), для которой существуют дополнительные сведения (любой другой формат) в конкретной папке (label*),
и сфомировать связь в виде ключ-значение, где ключ - метадата (.json), значение - список доп. сведений

Если для метадаты нет доп. сведений, она не учитывается.
"""


import os


labels_dir = "/tmp/labels"
os.makedirs(labels_dir, exist_ok=True)
labels = {"label1": ["1image.JPG", "2.jpeg", "2.json", "1image.json", "3.jpg"],
          "label2": ["1.jpg", "1.json", "2.json", "3.json"],
          "label3": ["15.png", "15.json", "16.json", "16.jpg", "1.PNG", "1.JSON"],
          "label4": ["1.png", "1.txt", "2.txt", ], }

for label in labels:
    label_path = os.path.join(labels_dir, label)
    os.makedirs(label_path, exist_ok=True)

    for item in labels[label]:
        open(os.path.join(label_path, item), 'a').close()

    print(f"{label_path} {os.listdir(label_path)}")

open(os.path.join(labels_dir, "test.txt"), 'a').close()


start_path = os.path.join(os.path.sep, 'tmp', 'labels')
result = list()


for i_elem in sorted(os.listdir(start_path)):
    crt_path = os.path.join(start_path, i_elem)
    if os.path.isdir(crt_path):
        json_files = list()
        other = list()
        [json_files.append(x) if '.json' in x.lower() else other.append(x) for x in os.listdir(crt_path)]

        dir_dict = dict()
        for i_file in json_files:
            for j_file in other:
                if i_file.split('.')[0] == j_file.split('.')[0]:
                    dir_dict[i_elem] = dir_dict.get(i_elem, list()) + [[j_file, i_file]]

        if dir_dict:
            result.append(dir_dict)


print(result)

# на случай, если результат нужно было записать в файл
# with open(os.path.join(labels_dir, "test.txt"), 'a') as file:
#     file.write(str(result))
# или json.dump(result, file)
