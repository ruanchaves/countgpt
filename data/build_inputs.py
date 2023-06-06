import os

def add_numbers(input_file, output_file):

    model_input = []
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            model_input.append(line)
    
    for idx, line in enumerate(model_input):
        new_line = f"{idx+1}. {line}"
        model_input[idx] = new_line

    with open(output_file, "w") as f:
        for idx, line in enumerate(model_input):
            if idx == len(model_input) - 1:
                f.write(f"{line}")
                break
            f.write(f"{line}\n")


def main():
    if os.path.exists("data/v7w_telling/v7w_telling_prompts.csv"):
        add_numbers("data/v7w_telling/v7w_telling_prompts.csv", "data/declarative/inputs.txt")

    if os.path.exists("data/declarative/outputs.txt"):
        add_numbers("data/declarative/outputs.txt", "data/entailment/inputs.txt")

if __name__ == "__main__":
    main()