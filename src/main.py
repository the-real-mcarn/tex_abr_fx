import re
import argparse
import os
import json

print("--- Cool latex abbreviation finder ---")

parser = argparse.ArgumentParser()
parser.add_argument("folder", help="Path to find text files")
parser.add_argument("--make-tex", help="Make a tex file with the abbreviations")
parser.add_argument("--output", help="Output path, default is output in this repo", default="output")
args = parser.parse_args()

if os.path.isabs(args.output):
    outputpath = args.output
else:
    outputpath = os.path.join(os.getcwd(), args.output)
print(f"Output will be saved in {outputpath}")

def main():
    tex_files = []
    
    if os.path.isabs(args.folder):
        basepath = args.folder
    else:
        basepath = os.path.join(os.getcwd(), args.folder)
    print(f"Looking for tex files in {basepath} \n\nFound files:")
    
    for root, dirs, files in os.walk(basepath):
        for file in files:
            if file.endswith(".tex"):
                result = os.path.join(root, file)
                tex_files.append(result)
                print(result)
    
    output = []
    total = 0 
    
    try:
        for path in tex_files: 
            file = open(path, "rt")

            for line in file:
                data = file.readline()

                # attempt to remove inline comments
                if "%" in data:
                    data = data.split("%")[0]

                regex = re.findall(r'(?<!\\)(\b|(?={))([A-Z]{2,})\b', data) 

                if regex != []:
                    for match in regex:
                        total += 1
                        if match[1] not in output:
                            output.append(match[1])

        output.sort()
        file.close()

        print(f"\nTotal found: {total}")
        print(f"Total unique: {len(output)}\n")
        print(output)
        
        jsonresult = json.dumps({value: "" for value in output}, indent=4)
        with open(os.path.join(outputpath, "abbreviations.json"), "w") as outfile:
            outfile.write(jsonresult)
            outfile.close()
        
    except Exception as e:
        print(e)
        print("Now fix it")
        return
    
def make_tex():
    print("Making tex file")
    return
        
if __name__ == "__main__":
    if args.make_tex:
        make_tex()
    else:
        main()