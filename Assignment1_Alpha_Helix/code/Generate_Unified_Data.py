import os
import json

def getFileIndex(index: int) -> str:
     if(index < 10):
          file_index = "00" + str(index)
     elif(index < 100):
          file_index = "0" + str(index)
     else:
          file_index = str(index)
     return file_index

def extract_info_from_first_corpus(base: str, num: int) -> list:
     # initialize data
     data = []
     for i in range(1, num+1):

          essay = {"id": 0,
                   "text": "",
                   "major_claim": [],
                   "claims": [],
                   "premises": [],
                   "confirmation_bias": None,
                   "paragraphs": []}

          file_name = base + "/data/ArgumentAnnotatedEssays-2.0/brat-project-final/essay"
          file_index = getFileIndex(i)

          # set essay id
          essay["id"] = i

          # set essay text
          with open(file_name + file_index + ".txt", "r") as f:
               text = f.readlines()
               text = "".join(text[i] for i in range(len(text)))
               essay["text"] = text.strip()

          # read the file essayxxx.ann to extract the info: MajorClaim, Claim, Premise
          with open(file_name + file_index + ".ann", "r") as f:
               major_claims = []
               claims = []
               premises = []
               for line in f.readlines():
                    dict = {"span": [], "text": ""}
                    if (line.split()[1] == "MajorClaim"):
                         dict["span"].append(int(line.split()[2]))
                         dict["span"].append(int(line.split()[3]))
                         dict["text"] = " ".join(line.split()[i] for i in range(4, len(line.split())))
                         essay["major_claim"].append(dict)
                    if (line.split()[1] == "Claim"):
                         dict["span"].append(int(line.split()[2]))
                         dict["span"].append(int(line.split()[3]))
                         dict["text"] = " ".join(line.split()[i] for i in range(4, len(line.split())))
                         essay["claims"].append(dict)
                    if (line.split()[1] == "Premise"):
                         dict["span"].append(int(line.split()[2]))
                         dict["span"].append(int(line.split()[3]))
                         dict["text"] = " ".join(line.split()[i] for i in range(4, len(line.split())))
                         essay["premises"].append(dict)
               data.append(essay)

     return data

def extract_info_from_second_corpus(base:str, data:list ) -> list:
     file_name = base + "/data/UKP-InsufficientArguments_v1.0/data-tokenized.tsv"
     with open(file_name, "r", errors="ignore") as f:
          f.readline()
          for line in f.readlines():
               para = {"text": "", "sufficient": None}
               id = int(line.split('\t')[0])
               para["text"] = line.split('\t')[2]
               if ("insufficient" in line.split('\t')[3]):
                    para["sufficient"] = False
               else:
                    para["sufficient"] = True
               data[id-1]["paragraphs"].append(para)
     return data

def extract_info_from_third_corpus(base: str, data: list) -> list:
     file_name = base + "/data/UKP-OpposingArgumentsInEssays_v1.0/labels.tsv"
     with open(file_name, "r") as f:
          f.readline()
          for i in range(0, 402):
               line = f.readline()
               if(line.split()[1]=="positive"):
                    data[i]["confirmation_bias"] = True
               elif(line.split()[1]=="negative"):
                    data[i]["confirmation_bias"] = False
     return data


if __name__ == '__main__':

     # extract info of all essays
     base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     data = extract_info_from_first_corpus(base, 402)
     data = extract_info_from_second_corpus(base, data)
     data = extract_info_from_third_corpus(base, data)

     # write info in to json file
     json_data = json.dumps(data, indent=4)
     json_file = base + "/data/unified_data_file.json"
     with open(json_file, 'w') as f:
          f.write(json_data)
     print("unified_data_file.json has been generated!")


